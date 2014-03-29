import tornado
from tornado.options import define, options
import tornado.web
import tornado.httpserver
import tornado.ioloop
import os.path

__author__ = 'dolel'

define("port", default=8500, help="Run the App on the Given Port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html', title="GeekNight Recommendation Engine")


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/", IndexHandler),
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True
    )
    tornado.httpserver.HTTPServer(app).listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
