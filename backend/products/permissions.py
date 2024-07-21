from rest_framework.permissions import DjangoModelPermissions, SAFE_METHODS

class MyCustomPermissionClass(DjangoModelPermissions):

	# perms_map = {
	# 	'GET': ['%(app_label)s.view_%(model_name)s'],
	# 	'OPTIONS': ['%(app_label)s.view_%(model_name)s'],
	# 	'HEAD': ['%(app_label)s.view_%(model_name)s'],
	# 	'POST': ['%(app_label)s.add_%(model_name)s'],
	# 	'PUT': ['%(app_label)s.change_%(model_name)s'],
	# 	'PATCH': ['%(app_label)s.change_%(model_name)s'],
	# 	'DELETE': ['%(app_label)s.delete_%(model_name)s'],
	# }

	def has_permission(self, request, view):
		# if request.method in SAFE_METHODS:
		# 	print(f"user request: ==> {request.user}")
		# 	return True
		return super().has_permission(request, view)

