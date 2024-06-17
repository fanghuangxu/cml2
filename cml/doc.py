def get_minecraft_docs(version:str):
    # 目标URL
    url = 'https://zh.minecraft.wiki/w/Java版{version}'
    import web
    web.show_url(url.format(version=version))


