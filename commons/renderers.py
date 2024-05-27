from rest_framework.renderers import JSONRenderer


class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_data = {
            "code": renderer_context["response"].status_code,
            "author": "jiwonman",
            "data": data
        }

        # if data.get("error"):
        #     response_data["error"] = data["error"]
        # else:
        #     response_data["data"] = data

        return super().render(response_data, accepted_media_type, renderer_context)
