import os
import sys
import glob
import textwrap
import shutil
import multiprocessing


class PythonFileProcessor:
    def __init__(self, source_folder: str):
        self.source_folder = source_folder

    def __enter__(self):
        print("\033[34m欢迎使用Python作业处理器！\n\033[0m")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(
                "\033[31m在处理数据时发生了意外错误。请检查输入参数并重试。如果问题仍然存在，请联系技术支持以获取进一步的帮助。\033[0m")
        return False

    def _view_file(self, text: str):
        """
        这是一个预览文件的函数。
        :param text: 文件的全部内容
        :return: None
        """
        short_text = textwrap.shorten(text, width=50)
        print(short_text)

    def _run_code(self, code: str, file: str, output_pipe):
        """
        这是一个运行文件中Python代码的函数
        :param code: 代码
        :param file: 文件名称
        :return: 是否出现错误
        """
        result = True
        try:
            print("\033[32m代码输出：\033[0m")
            exec(code)
        except Exception as e:
            print("\033[1m\033[31m文件 {0} 无法运行!\n\033[0m".format(file))
            result = False
        output_pipe.send(result)
        output_pipe.close()

    def _check_code(self, code: str, py_file: str, timeout: int):
        """
        这是一个检查代码是否合理的函数
        :param code: 代码
        :param py_file: py文件名称
        :param timeout: 超时秒数
        :return: 是否出现错误
        """
        result = True
        print("\033[34m开始执行文件 {0} 代码检测\033[0m".format(py_file))
        print("\033[32m文件预览：\033[0m")
        self._view_file(code)
        parent_conn, child_conn = multiprocessing.Pipe()
        p = multiprocessing.Process(target=self._run_code, args=(code, py_file, child_conn))
        p.start()
        p.join(timeout)
        if p.is_alive():
            p.terminate()
            p.join()
            result = False
            output = False
            print("\033[1m\033[31m文件 {0} 运行超时！\n\033[0m".format(py_file))
        else:
            output = parent_conn.recv()
            if output:
                print("\033[34m文件 {0} 检测通过！\n\033[0m".format(py_file))
        if result and output:
            return True
        return False

    def _move_dir(self, target_folder: str = os.getcwd() + r"\作业", new_folder: bool = True,
                  deep_search: bool = False):
        """
        这是一个移动文件夹中Python文件的函数，用于便于统计Python作业
        :param target_folder: 移动的目标文件夹
        :param new_folder: 是否新建文件夹。如果是，则根据target_folder新建文件夹，如果不是，则需目标路径存在
        :param deep_search: 是否进行深度搜索
        :return: None
        """
        if new_folder:
            if not os.path.exists(target_folder):
                os.mkdir(target_folder)

        if not os.path.exists(target_folder):
            raise FileExistsError(
                "\033[31m您要访问的路径不存在或非空。请验证路径并重试。如果问题仍然存在，请确保文件未被移动、重命名或删除，并检查当前用户对文件的权限。\033[0m")

        if_empty = True
        if deep_search:
            file_paths = glob.glob("{0}/**/*.py".format(self.source_folder), recursive=True)
        else:
            file_paths = glob.glob("{0}/*.py".format(self.source_folder), recursive=False)
        for file in file_paths:
            if_empty = False
            shutil.move(file, target_folder)
            print("\033[32m已成功将文件 {0} \n移动到文件夹 {1}\n\033[0m".format(file, target_folder))

        if if_empty:
            print("\033[1m\033[31m警告！文件夹 {0} 中不存在Python文件！\033[0m".format(self.source_folder))

        self.source_folder = target_folder
        print("\033[1m\033[34m已成功更新工作目录 {0}\n\033[0m".format(self.source_folder))

    def statistic_line_num(self, include_comments: bool = True, correct_error: bool = False, timeout: int = 5, **args):
        """
        这是一个统计工作目录下Python文件行数的函数，其计算结果可用来衡量学生工作量
        :param include_comments: 是否计算注释行
        :param correct_error: 是否检查Python代码能否执行(请提前准备好作业依赖库)
        :param timeout: 代码执行超时时间(防止恶意循环)
        :return: 代码的总行数
        """
        self._move_dir(**args)
        num = 0
        file_paths = [os.path.join(self.source_folder, file) for file in os.listdir(self.source_folder)]
        for py_file in file_paths:
            with open(py_file, mode="r", encoding="utf-8") as file:
                code = file.read()
                if correct_error:
                    answer = self._check_code(code, py_file, timeout)
                if answer:
                    lines = code.splitlines()
                    lines = [line for line in lines if (include_comments or (not line.startswith("#"))) and line.strip()]
                    num += len(lines)
        return num


if __name__ == '__main__':
    with PythonFileProcessor("我的作业") as py_processor:
        num = py_processor.statistic_line_num(correct_error=True, deep_search=True)
        print(f"代码总数为：{num}")
