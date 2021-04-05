#! /usr/bin/env python  
# -*- coding:utf-8 -*-  
# ====#====#====#====
__author__ = "FogSong"

# FileName: pic.py  `
# Version:1.0.0  `
# ====#====#====#====

import base64,time
import requests


class Pic(object):

    def __init__(self, token: str, owner: str, repo: str):
        self.token = token
        self.owner = owner,
        self.repo = repo
        self.upload_url = "https://gitee.com/api/v5/repos/%s/%s/contents/" % (owner, repo)

    def upload(self, file_path: str, path: str, message: str = "pic"):
        with open(file_path, "rb") as pic:
            base64_data: str = base64.b64encode(pic.read()).decode(encoding = "utf-8")
            return self.__upload(base64_data, path, message)

    def upload_with_time_path(self, file_path: str, message: str = "pic"):
        path: str = f"{time.strftime(r'%Y/%m/%d/%H')}.{file_path.split('.')[1]}"
        return self.upload(file_path, path, message)

    def __upload(self, base64_data: str, path, message: str):
        url = f"{self.upload_url}{path}"
        result: dict = requests.post(url, data = {
            "access_token": self.token,
            "content": base64_data,
            "message": message
        }).json()
        content: dict = result.get("content",None)
        if content:
            pic_url = content.get("download_url", None)
            if pic_url:
                return pic_url
        return result["message"]



