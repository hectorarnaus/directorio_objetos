from wordpress_xmlrpc import AuthenticatedMethod

class SetAttachmentAltText(AuthenticatedMethod):
    method_name = "media.set_alt_text"
    method_args = ("attachment_id", "alt_text")