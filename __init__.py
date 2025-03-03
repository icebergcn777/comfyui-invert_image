from .invert_image_node import InvertImageNode

NODE_CLASS_MAPPINGS = {
    "Invert Image Node Sample": InvertImageNode
    }

__all__ = ["NODE_CLASS_MAPPINGS"]

'''ここでは、キーとなる文字列"Invert Image Node Sample"がComfyUI内部でのノード名として扱われます。後でUIの「Add Node」メニューにこの名前が現れるわけです。InvertImageNodeクラスは、レジストリを辿って読み込まれていきます。'''