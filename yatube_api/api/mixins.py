from rest_framework import mixins, viewsets
from rest_framework.exceptions import PermissionDenied


class UpdateDestroyViewSet(viewsets.ModelViewSet):
    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(UpdateDestroyViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(UpdateDestroyViewSet, self).perform_destroy(instance)


class ReadCreateViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    pass
