================
ZCool Downloader
================


.. image:: https://img.shields.io/pypi/v/zcooldl.svg
        :target: https://pypi.python.org/pypi/zcooldl

.. image:: https://img.shields.io/travis/lonsty/zcooldl.svg
        :target: https://travis-ci.org/lonsty/zcooldl

.. image:: https://readthedocs.org/projects/zcooldl/badge/?version=latest
        :target: https://zcooldl.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/lonsty/zcooldl/shield.svg
     :target: https://pyup.io/repos/github/lonsty/zcooldl/
     :alt: Updates



ZCool picture crawler. Download ZCool (https://www.zcool.com.cn/) Designer's or User's pictures, photos and illustrations.


* Free software: MIT license
* Documentation: https://zcooldl.readthedocs.io.


Features
--------

* 极速下载：多线程异步下载，可以根据需要设置线程数
* 异常重试：只要重试次数足够多，就没有下载不下来的图片 \(^o^)/！
* 增量下载：设计师/用户有新的上传，再跑一遍程序就行了 O(∩_∩)O 嗯！
* 自选主题：可以选择下载用户的特定主题，而不是该用户下的所有内容
* 下载收藏夹 `New`：使用 `-c <收藏夹 URL, ...>` 下载收藏夹中的作品（收藏夹可自由创建）

Quickstart
----------

Install zcooldl via pip:

.. code-block:: console

    $ pip install -U zcooldl

Download all username's pictures to current directory:

.. code-block:: console

    $ zcooldl -u <username>

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
