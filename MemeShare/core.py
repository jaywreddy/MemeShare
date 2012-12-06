import json
import marshal
import uuid
from models import *

def create_meme(image, memegroup):
    image_id=generate_uuid()
    #store image with image id
    #print(cloudinary.uploader.upload(image, public_id= image_id))
    Meme(meme_id = image_id, memegroup_id = memegroup).save()
    return image_id

def add_user_to_memegroup(user_id, memegroup_id):
    user_association(user_id=user_id, memegroup_id=memegroup_id).save()


def create_memegroup(name):
    memegroup_id=generate_uuid()
    MemeGroup(memegroup_id=memegroup_id, memegroup_name=name).save()
    return memegroup_id

def get_user_memegroups(user_id):
    memegroups=user_association.objects.filter(user_id=user_id)
    grouplist=[]
    for memegroup in memegroups:
        memegroup_id=memegroup.memegroup_id
        name=get_memegroup_name(memegroup_id)
        grouplist.append(memegroup_id, name)
    if len(grouplist)==0:
        return None
    return json.dumps(grouplist)

def get_memegroup_name(memegroup_id):
    memegroups=MemeGroup.objects.filter(memegroup_id=memegroup_id)
    name=''
    for memegroup in memegroups:
        name= memegroup.memegroup_name
    return name

def get_memegroup_memes(memegroup_id):
    memes= Meme.objects.filter(memegroup_id=memegroup_id)
    memelist=[]
    for meme in memes:
        memelist.append(meme.meme_id)
    if len(memelist)==0:
        return None
    return json.dumps(memelist)

def generate_uuid():
    id=uuid.uuid4().hex
    return id
