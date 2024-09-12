import sys

import texthandler


# 获取命令行参数
def get_args():
    args = []
    try:
        if len(sys.argv) < 4:
            raise ValueError
        else:
            for i in range(1, 4):
                if isinstance(sys.argv[i], str):
                    args.append(sys.argv[i])
                else:
                    raise TypeError
    except ValueError:
        print("请输入正确的参数个数")
        return ValueError
    except TypeError:
        print("请输入正确的参数类型")
        return TypeError
    return args


def paper_check():
    # 测试文件路径
    orig_path = "D:/PycharmProjects/3122004316/test/orig.txt"
    orig_add_path = "D:/PycharmProjects/3122004316/test/orig_0.8_add.txt"
    answer_path = "D:/PycharmProjects/3122004316/test/ans.txt"
    # 获取命令行参数
    # args_list = get_args()
    # orig_path, orig_add_path, answer_path = args_list[0], args_list[1], args_list[2]
    # 读取文件并过滤标点符号
    file1, file2 = texthandler.file_handle(orig_path, orig_add_path)
    # 进行内容分词
    string1, string2 = texthandler.segment(file1, file2)
    # 分词转化为向量，降低维度分析
    orig_feature, orig_add_feature = texthandler.vector_transform(string1, string2)
    # 计算向量夹角余弦值，得余弦相似度
    result = texthandler.calculate_cos_similarity(orig_feature, orig_add_feature)
    # 将结果保存到文件中
    print(result)
    texthandler.save_file(answer_path, result)


# 主函数，程序的入口
if __name__ == '__main__':
    paper_check()
