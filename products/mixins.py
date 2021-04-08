from django.http import Http404


class IsOwnerMixin:
    """
    Check's if request.user is requested object owner.
    If not, Http404 error raised.
    """

    def get_object(self, *args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        if not obj.owner == self.request.user:
            raise Http404
        return obj
