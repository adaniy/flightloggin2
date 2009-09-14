from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from django.http import HttpResponse

class plot_png(object):
    def __init__(self, view):
        self.view = view
    
    def __call__(self, *args, **kwargs):
        fig = self.view(*args, **kwargs)
        canvas=FigureCanvas(fig)
        response=HttpResponse(content_type='image/png')
        canvas.print_png(response)
        return response
        
class plot_svg(object):
    def __init__(self, view):
        self.view = view
    
    def __call__(self, *args, **kwargs):
        fig = self.view(*args, **kwargs)
        canvas=FigureCanvas(fig)
        response=HttpResponse(content_type='image/svg+xml')
        canvas.print_svg(response)
        return response
    
class plot_png2(object):
    def __init__(self, view):
        self.view = view
    
    def __call__(self, *args, **kwargs):
        fig = self.view(*args, **kwargs)
        response=HttpResponse(content_type='image/png')
        fig.savefig(response, format="png", bbox_inches="tight", pad_inches=.05, edgecolor="white")
        return response
    
class plot_svg2(object):
    def __init__(self, view):
        self.view = view
    
    def __call__(self, *args, **kwargs):
        fig = self.view(*args, **kwargs)
        response=HttpResponse(content_type='image/svg+xml')
        fig.savefig(response, format="svg", bbox_inches="tight", pad_inches=.05, edgecolor="white")
        return response
