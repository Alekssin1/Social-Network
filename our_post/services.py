from our_post.models import Photo


def save_form_db(key, request, post_form) -> None:
    form_data = post_form.save(commit=False)
    form_data.userId = request.user
    post_form.cleaned_data
    form_data.save()
    #  збереження фотографій в базі даних
    for i in request.FILES.getlist(key):
        form_data.content.add(Photo.objects.create(photo=i))
    form_data.save()
    
    
def dict_with_user_and_id_post(all_obj, all_obj_db)-> None:
    for obj in all_obj_db:
        if all_obj.get(obj.postId_id, False):
            all_obj[obj.postId_id].append(obj.userId_id)
        else:
            all_obj[obj.postId_id] = [obj.userId_id]
            
def count_elem(all_like, my_like) -> None:
    for key, value in all_like.items():
        my_like[key] = len(value)
        