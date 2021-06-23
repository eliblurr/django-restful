from rest_framework.response import Response
from .serializers import SnippetSerializer
from rest_framework.views import APIView
from django.http import Http404, HttpResponse
from .models import Snippet

def index(request):
    print(dir(request.user))
    return HttpResponse('django simple api with restful', status=200)

class SnippetView(APIView):
    serializer = SnippetSerializer
    model = Snippet
    
    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404
    
    def get(self, request, pk=0):
        pk, limit, offset, value, search = pk or request.GET.get('pk'), request.GET.get('limit', 100),  request.GET.get('offset', 0), request.GET.get('value', None), request.GET.get('search', None)
        base = self.serializer(self.model.objects.all()[offset:offset+limit], many=True)
        if pk:
            base = self.serializer(self.get_object(pk))
        elif search and value:
            try:
                base = self.serializer(self.model.objects.filter(**{search+'__contains':value})[offset:offset+limit], many=True)
            except:
                pass            
        return Response(base.data)

    def post(self, request):
        serializer = self.serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def put(self, request, pk):
        serializer = self.serializer(self.get_object(pk), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=202)

    def patch(self, request, pk):
        serializer = self.serializer(self.get_object(pk), data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=202)
    
    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=204)