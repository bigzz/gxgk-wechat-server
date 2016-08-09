#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import celery, app
from ..utils import AESCipher, update_wechat_token


@celery.task(name='access_token.update')
def update_access_token():
    """定时更新微信 access_token，写入缓存"""
    update_wechat_token()
