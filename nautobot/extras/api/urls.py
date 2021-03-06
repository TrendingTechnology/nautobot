from nautobot.core.api import OrderedDefaultRouter
from . import views


router = OrderedDefaultRouter()
router.APIRootView = views.ExtrasRootView

# Custom fields
router.register("custom-fields", views.CustomFieldViewSet)

# Export templates
router.register("export-templates", views.ExportTemplateViewSet)

# Tags
router.register("tags", views.TagViewSet)

# Git repositories
router.register("git-repositories", views.GitRepositoryViewSet)

# Image attachments
router.register("image-attachments", views.ImageAttachmentViewSet)

# Config contexts
router.register("config-contexts", views.ConfigContextViewSet)

# Jobs
router.register("jobs", views.JobViewSet, basename="job")

# Change logging
router.register("object-changes", views.ObjectChangeViewSet)

# Job Results
router.register("job-results", views.JobResultViewSet)

# ContentTypes
router.register("content-types", views.ContentTypeViewSet)

# Custom Links
router.register("custom-links", views.CustomLinkViewSet)

# Webhooks
router.register("webhooks", views.WebhooksViewSet)

# Statuses
router.register("statuses", views.StatusViewSet)

# Relationships
router.register("relationships", views.RelationshipViewSet)
router.register("relationship-associations", views.RelationshipAssociationViewSet)

app_name = "extras-api"
urlpatterns = router.urls
