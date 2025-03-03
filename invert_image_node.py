#受け取ったIMAGEを反転して返す

import torch

class InvertImageNode:
    # カテゴリ名。UIの「Add Node」メニューでの配置先。
    CATEGORY = "example"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image_in": ("IMAGE", {})
                }
            }

        # 出力はIMAGE型を1つ返す
        RETURN_TYPES = ("IMAGE", )
        RETURN_NAMES = ("image_out", ) # 出力スロットに付けるラベル(省略可)
        FUNCTION = "invert"

    def invert(self, image_in):
        # image_inはtorch.Tensor ([B,H,W,C]) で来る
        # 0~1で正規化されているので、1 - values でピクセル反転可能
        image_out = 1.0 - image_in
        return (image_out,)
    
#CATEGORY: "example"というカテゴリ名。
#INPUT_TYPES: "required"パラメータとして"image_in": ("IMAGE", {})を1つ準備。
#FUNCTION: このクラスのinvertメソッドを実行メソッドに指定。
#invertメソッド: 第1引数にself、第2引数にINPUT_TYPESで定義したimage_inを受け取り、処理結果をタプル(image_out,)で返す。