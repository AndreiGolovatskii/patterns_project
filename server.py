import logging

import attr
from aiohttp import web


from default_game.default_game import get_default_game
from libs.visitor.visitor import Visitor

async def index(request):
    with open('web/main.html') as page:
        return web.Response(body=page.read(), content_type='text/html')
    return web.Response(status=500)


async def get_file(request):
    with open('web/{}'.format(request.match_info['file_path']), 'r') as jquery:
        return web.Response(body=jquery.read(), content_type='text')
    return web.Response(status=500)


async def get_asset(request):
    with open('web/assets/{}'.format(request.match_info['name']), 'rb') as jquery:
        return web.Response(body=jquery.read(), content_type='img')
    return web.Response(status=500)


@attr.s
class GameManager:
    game = attr.ib(factory=get_default_game)

    async def action(self, request):
        self.game.add_action_from_json(await request.json())
        return web.Response(status=200)

    async def get_game(self, request):
        visitor = Visitor()
        self.game.visit(visitor)

        self.game.iteration()

        return web.json_response(visitor.j)


def main():
    logging.basicConfig(level=logging.ERROR)
    game = GameManager()

    app = web.Application()
    app.router.add_get('/', index)
    app.router.add_get('/{file_path}', get_file)
    app.router.add_get('/assets/{name}', get_asset)

    app.router.add_post('/action', game.action)
    app.router.add_post('/get_game', game.get_game)

    web.run_app(app)


if __name__ == '__main__':
    main()
