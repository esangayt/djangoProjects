from rest_framework.renderers import JSONRenderer


class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = {
            "ok": renderer_context["response"].status_code < 400,
            "data": data
        }

        return super().render(response, accepted_media_type, renderer_context)
