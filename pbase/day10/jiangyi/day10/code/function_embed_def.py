# function_embed_def.py


# 此示例示意函数嵌套定义 


def fn_outer():
    print("fn_outer 被调用")
    def fn_inner():
        print("fn_inner 被调用")
    fn_inner()
    fn_inner()
    print("fn_outer 调用结束")

fn_outer()
print("程序结束")
