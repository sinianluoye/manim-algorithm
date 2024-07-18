import manim
from .utils.debug import index_code_labels

class Code(manim.Code):

    def __init__(self, *args, **kwargs):
        """
        一个用于展示代码的类，相比于manim.Code有一些额外的扩充, 包含三个子对象
        - background_mobject: 代码框的背景
        - line_numbers: 行号
        - code: 代码本身

        参数
        ----------
        file_name
            要显示的代码文件的名称。
        code
            如果没有指定``file_name``，可以直接传递一个代码字符串。
        tab_width
            一个制表符字符对应的空格字符数。默认为3。
        line_spacing
            行间距与字体大小的比例。默认为0.3，即字体大小的30%。
        font_size
            显示代码的缩放比例。默认为24。
        font
            要使用的文本字体的名称。默认为``"Monospace"``。
            这可以是系统字体或通过`text.register_font()`加载的字体。注意
            字体家族名称在不同操作系统中可能不同。
        stroke_width
            文本的描边宽度。推荐为0，默认也是0。
        margin
            文本与背景的内边距。默认为0.3。
        indentation_chars
            “缩进字符”指的是给定代码行开头的空格/制表符。默认为``"    "``（4个空格）。
        background
            定义背景的类型。目前仅支持``"rectangle"``（默认）和``"window(类似mac窗口)"``。
        background_stroke_width
            定义背景的描边宽度。默认为1。
        background_stroke_color
            定义背景的描边颜色。默认为``WHITE``。
        corner_radius
            定义背景的圆角半径。默认为0.2。
        insert_line_no
            定义是否在显示的代码中插入行号。默认为``True``。
        line_no_from
            定义行号计数的起始行号。默认为1。
        line_no_buff
            定义行号与显示代码之间的间距。默认为0.4。
        style
            定义显示代码的样式类型。你可以在:attr:`styles_list`中看到可能的样式名称。默认为``"monokai"``。
        language
            指定给定代码所使用的编程语言。如果为``None``
            （默认值），则会自动检测语言。要查看
            可能的选项，请访问https://pygments.org/docs/lexers/ 并查找
            '别名或简称'。
        generate_html_file
            定义是否在`assets/codes/generated_html_files`文件夹中生成高亮的html代码。默认为`False`。
        warn_missing_font
            如果为True（默认），当字体不存在于
            `manimpango.list_fonts()`返回的（区分大小写的）字体列表中时，Manim会发出警告。
        """
        if "style" not in kwargs:
            kwargs["style"] = "monokai"
        super().__init__(*args, **kwargs)
    
    def generate_index_labels(self, label_height: float = 0.1, **kwargs) -> manim.VGroup:
        """
        在代码上为每个字符生成标号, 便于定位字符

        Args:
            label_height (float, optional): 标号的高度. Defaults to 0.1.
        kwargs:
            标号为manim.Integer, 这些参数都会传递给manim.Integer
        Returns:
            manim.VGroup: 一个2D的manim.VGroup对象，第一层对应着每一行，第二层对应着标号
        """
        return index_code_labels(self, label_height=label_height, **kwargs)

class PythonCode(Code):

    def __init__(self, *args, **kwargs):
        if "language" not in kwargs:
            kwargs["language"] = "python"
        super().__init__(*args, **kwargs)

class JavaCode(Code):
    
    def __init__(self, *args, **kwargs):
        if "language" not in kwargs:
            kwargs["language"] = "java"
        super().__init__(*args, **kwargs)

class CppCode(Code):
    
    def __init__(self, *args, **kwargs):
        if "language" not in kwargs:
            kwargs["language"] = "cpp"
        super().__init__(*args, **kwargs)