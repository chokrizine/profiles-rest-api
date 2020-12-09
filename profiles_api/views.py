
from   rest_framework.views import APIView
from   rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    "Test APIview"

    def get(self,request,fomat=None):
        """return a list of APIVview features"""

        an_apiview=[
        'uses HTTP methods as function(get,post,patch,put,delete)',
        'is similar to a tradiutional django View',
        'Gives you the most control over you application logic',
        'Is mapped manually to URLs'
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})
