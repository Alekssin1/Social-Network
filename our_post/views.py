from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import Post_form
from our_post.models import UserPost, PostLikes, PostComment, Photo 
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
User = get_user_model()


# Create your views here.
def posts(request):
    # якщо спрацьовує метод POST значить відбулося відправлення форми з додавання посту
    if request.method == "POST":
        # зберігаю значення з форми в словник
        post_form = Post_form(request.POST, request.FILES)

        if post_form.is_valid():
            temp = post_form.save(commit=False)
            temp.userId = request.user
            post_form.cleaned_data
            temp.save()

            # збереження фотографій в базі даних
            for i in request.FILES.getlist("content"):
                temp.content.add(Photo.objects.create(photo=i))
            temp.save()
            return HttpResponseRedirect(request.path)
    else:
        id_post_like = []
        all_like = {}
        my_like = {}
        try:
            # зберігаєм лайки цього користувача
            like_this_user = PostLikes.objects.filter(userId_id=request.user)
            # записую в список айді всіх постів, до яких я поставив лайк
            for i in like_this_user:
                id_post_like.append(i.postId_id)
        # заходить в помилку, якщо в базі не знайшло лайків в даного користувача
        except Exception:
            pass

        # створює словник, ключем в якому є айді посту, а значеннями список
        # з користувачів які натиснули лайк
        all_like_post = PostLikes.objects.all()
        for like in all_like_post:
            if all_like.get(like.postId_id, False):
                all_like[like.postId_id].append(like.userId_id)
            else:
                all_like[like.postId_id] = [like.userId_id]

        # створює словник, в якому за ключем(айді посту), зберігається кількість лайків
        for key, value in all_like.items():
            my_like[key] = len(value)

        comment = PostComment.objects.order_by("id")
        all_comment = {}
        my_comment = {}
        
        # створює словник, ключем в якому є айді посту, а значеннями список
        # з користувачів які відправили комент
        for like in comment:
            if all_comment.get(like.postId_id, False):
                all_comment[like.postId_id].append(like.userId_id)
            else:
                all_comment[like.postId_id] = [like.userId_id]

        # створює словник, в якому за ключем(айді посту), зберігається кількість коментів
        for key, value in all_comment.items():
            my_comment[key] = len(value)

        post_form = Post_form()
        return render(request, 'our_post\main.html', context={'form': post_form, 'posts': UserPost.objects.order_by("-id"), 'like_posts': id_post_like, 'number_like': my_like, 'all_id_post': list(my_like.keys()), 'id_comment': my_comment})


def like(request):
    # отримання данних про натискання на лайк
    post_id = request.GET.get('result', False)
    data = {"like": False}
    temp = True

    try:
        # дістає об'єкт лайку до цього посту
        my_like = PostLikes.objects.get(
            postId_id=int(post_id), userId_id=request.user)
    except Exception:
        temp = False

    # якщо об'єкт не існує і лайк поставлений, то заносить данні в базу
    if post_id and not temp:
        my_user = UserPost.objects.get(id=int(post_id))
        post_like = PostLikes()
        post_like.userId = request.user
        post_like.postId = my_user
        post_like.save()
        data = {"like": True}
        return JsonResponse(data)

    # якщо запис є і натисуто повторно, видаляє цей лайк за бази
    if temp:
        my_like.delete()

    return JsonResponse(data)


@login_required(login_url="/accounts/login/")
def comments(request, post_id):
    comment = PostComment.objects.order_by("id")
    all_comment = {}
    my_comment = {}

    # створює словник, ключем в якому є айді посту, а значеннями список
    # з користувачів які відправили комент
    for like in comment:
        if all_comment.get(like.postId_id, False):
            all_comment[like.postId_id].append(like.userId_id)
        else:
            all_comment[like.postId_id] = [like.userId_id]

    # створює словник, в якому за ключем(айді посту), зберігається кількість коментів
    for key, value in all_comment.items():
        my_comment[key] = len(value)

    return render(request, 'our_post\post.html', context={'posts': UserPost.objects.get(id=int(post_id)), 'comments':PostComment.objects.filter(postId=int(post_id)) , 'id_comment': my_comment})
