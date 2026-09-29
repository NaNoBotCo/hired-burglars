import functools, http.server, pathlib, sys
here = pathlib.Path(__file__).resolve().parent.parent
port = int(sys.argv[1]) if len(sys.argv) > 1 else 8884
h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(here))
http.server.ThreadingHTTPServer(("127.0.0.1", port), h).serve_forever()
