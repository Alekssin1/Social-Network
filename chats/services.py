def set_name_group(obj_first, obj_second) -> str:
    if obj_first.user.id > obj_second.id:
        thread_name = f'chat_{obj_first.user.id}-{obj_second.id}'
    else:
        thread_name = f'chat_{obj_second.id}-{obj_first.user.id}'
    return thread_name