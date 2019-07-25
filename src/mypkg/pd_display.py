"""Customize display of pandas.DataFrame"""
import pandas as pd


class PandasDisplay:
    """Customize display"""
    custom_dict = {
        'max_rows': 200,  # 最大表示行数
        'max_columns': 100,  # 最大表示列数
        'width': 400,  # 全体の最大表示幅
        'max_colwidth': 50,  # 列ごとの最大表示幅
        'show_dimensions': True,  # 省略時の行数・列数表示
        'colheader_justify': 'right',  # 列名表示の右寄せ・左寄せ
        'precision': 6,  # 小数点以下の桁数
        'float_format': None  # 有効数字（有効桁数）
    }

    @classmethod
    def custom(cls):
        pd.options.display.max_rows = cls.custom_dict['max_rows']
        pd.options.display.max_columns = cls.custom_dict['max_columns']
        pd.options.display.width = cls.custom_dict['width']
        pd.options.display.show_dimensions = cls.custom_dict['show_dimensions']


if __name__ == '__main__':
    import inspect


    def _main():
        print('-' * 80)
        print(f">> pandas {pd.__version__}")
        print(f"\nDisplay Options")

        obj = pd.options.display
        default = inspect.getmembers(obj, inspect.ismethod(obj))

        PandasDisplay.custom()

        custom = inspect.getmembers(obj, inspect.ismethod(obj))

        for d, c in zip(default, custom):
            if d[1] != c[1]:
                print(f">> display.{d[0]}")
                print(f"\t\t Default : {d[1]}")
                print(f"\t\t Custom  : {c[1]}")


    _main()
