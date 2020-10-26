from dry_rest_permissions.generics import DRYPermissions
from rest_framework.viewsets import ModelViewSet

from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer, CategoryReadSerializer
from apps.core.views import MultiSerializerMixin


class CategoryViewSet(MultiSerializerMixin, ModelViewSet):
    """
        ViewSet based on Category model.

        list: List every Category.

        This route doesn't allow to filter,search or order requests.

        retrieve: Retrieve specific instance of category.

        To correct response you need provide *id* of existing category instance in path.

        update: Update category instance informations.

        To correct response you need provide *id* of existing category instance in path.

        create: Create new category.

        To successfuly add new beacon check BeaconSerializer for needed fields and its additional parameters.

        partial_update: Patch category.

        To correct response you need provide *id* of existing category instance in path.

        destroy: Delete category.

        To correct response you need provide *id* of existing category instance in path.
        """
    permission_classes = (DRYPermissions,)
    queryset = Category.objects.all()

    serializers = {
        'create': CategorySerializer,
        'update': CategorySerializer,
        'partial_update': CategorySerializer,
        'default': CategoryReadSerializer
    }
