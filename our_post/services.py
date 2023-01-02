from our_post.models import Photo, PostLikes, UserPost


def save_form_db(key, request, post_form) -> None:
    form_data = post_form.save(commit=False)
    form_data.userId = request.user
    post_form.cleaned_data
    form_data.save()
    #  збереження фотографій в базі даних
    for i in request.FILES.getlist(key):
        form_data.content.add(Photo.objects.create(photo=i))
    form_data.save()
    
def id_post_with_like_to_list(id_post_like: dict, request) -> None:
    try:
        # зберігаєм лайки цього користувача
        like_this_user = PostLikes.objects.filter(userId_id=request.user)
        # записую в список айді всіх постів, до яких я поставив лайк
        for i in like_this_user:
            id_post_like.append(i.postId_id)
    # заходить в помилку, якщо в базі не знайшло лайків в даного користувача
    except Exception:
        pass
    
def dict_with_user_and_id_post(all_obj, all_obj_db)-> None:
    for obj in all_obj_db:
        if all_obj.get(obj.postId_id, False):
            all_obj[obj.postId_id].append(obj.userId_id)
        else:
            all_obj[obj.postId_id] = [obj.userId_id]
            
def count_elem(all_like, my_like) -> None:
    for key, value in all_like.items():
        my_like[key] = len(value)
        
def like_to_db(request, post_id):
    my_user = UserPost.objects.get(id=int(post_id))
    post_like = PostLikes()
    post_like.userId = request.user
    post_like.postId = my_user
    post_like.save()
    return {"like": True}