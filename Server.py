import tornado.ioloop
import tornado.web

import Database


class LastData( tornado.web.RequestHandler ):
    def get(self):
        #self.write("Hello, world")
        
        self.write(database.getLastData())


class SomeData( tornado.web.RequestHandler ):
    def get(self):
        self.write("plug_id: a b i e --- state: 0 1")
    
    
    def post(self):
        plug_id = self.get_argument('plug_id')
        state  = self.get_argument('state')



application = tornado.web.Application([
    (r"/last/", LastData),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
