from bottle import route, run, template, TEMPLATE_PATH, static_file
import os

class Client:
    views_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'views')
    TEMPLATE_PATH.insert(0 ,views_path)
    @route('/criptoink')
    def index():
        return template('dashboard')

    @route('/assets/<filepath:path>', name='assets')
    def server_static(filepath):
        return static_file(filepath, root=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'views/assets'))

    def go_to_live():
        run(host='localhost', port=8080)
