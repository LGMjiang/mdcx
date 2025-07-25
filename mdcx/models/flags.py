from asyncio import Event
from dataclasses import dataclass, field
from typing import Any

from mdcx.models.enums import FileMode
from mdcx.models.types import ScrapeResult


@dataclass
class _Flags:
    # 指定刮削 #todo 改为传参
    appoint_url: str = ""
    website_name: str = ""

    # 刮削相关
    rest_time_convert: int = 0
    rest_time_convert_: int = 0
    total_kills: int = 0
    now_kill: int = 0
    success_save_time: float = 0.0
    next_start_time: float = 0.0
    count_claw: int = 0  # 批量刮削次数
    can_save_remain: bool = False  # 保存剩余任务
    remain_list: list[str] = field(default_factory=list)
    new_again_dic: dict[str, tuple[str, str, str]] = field(default_factory=dict)
    again_dic: dict[str, tuple[str, str, str]] = field(default_factory=dict)  # 待重新刮削的字典
    start_time: float = 0.0
    file_mode: FileMode = FileMode.Default  # 默认刮削待刮削目录
    counting_order: int = 0  # 刮削顺序
    total_count: int = 0  # 总数
    rest_now_begin_count: int = 0  # 本轮刮削开始统计的线程序号（实际-1）
    sleep_end: Event = field(default_factory=Event)  # 本轮休眠标识
    rest_next_begin_time: float = 0.0  # 下一轮开始时间
    scrape_starting: int = 0  # 已进入过刮削流程的数量
    scrape_started: int = 0  # 已进入过刮削流程并开始的数量
    scrape_done: int = 0  # 已完成刮削数量
    succ_count: int = 0  # 成功数量
    fail_count: int = 0  # 失败数量
    # 所有文件最终输出路径的字典（如已存在，则视为重复文件，直接跳过）
    file_new_path_dic: dict[str, list[str]] = field(default_factory=dict)
    # 当前文件的图片最终输出路径的字典（如已存在，则最终图片文件视为已处理过）
    pic_catch_set: set[str] = field(default_factory=set)
    # 当前番号的图片已下载完成的标识（如已存在，视为图片已下载完成）
    file_done_dic: dict[str, dict[str, str]] = field(default_factory=dict)
    # 当前文件夹剧照已处理的标识（如已存在，视为剧照已处理过）
    extrafanart_deal_set: set[str] = field(default_factory=set)
    # 当前文件夹剧照副本已下载的标识（如已存在，视为剧照已处理过）
    extrafanart_copy_deal_set: set[str] = field(default_factory=set)
    # 当前文件trailer已处理的标识（如已存在，视为剧照已处理过）
    trailer_deal_set: set[str] = field(default_factory=set)
    # 当前文件夹剧照已下载的标识（如已存在，视为剧照已处理过）
    theme_videos_deal_set: set[str] = field(default_factory=set)
    # 当前文件nfo已处理的标识（如已存在，视为剧照已处理过）
    nfo_deal_set: set[str] = field(default_factory=set)
    # 去获取json的番号列表
    json_get_set: set[str] = field(default_factory=set)
    # 获取成功的json
    json_data_dic: dict[str, ScrapeResult] = field(default_factory=dict)
    img_path: str = ""
    # 失败文件和错误原因记录
    failed_list: list[list[str]] = field(default_factory=list)
    # 失败文件记录
    failed_file_list: list[str] = field(default_factory=list)
    scrape_start_time: float = 0.0
    success_list: set[str] = field(default_factory=set)
    stop_other: bool = True  # 非刮削线程停止标识

    # show
    log_txt: Any = None  # 日志文件对象
    scrape_like_text: str = ""
    main_mode_text: str = ""

    single_file_path: str = ""  # 工具-单文件刮削的文件路径

    # for missing
    local_number_flag: str = ""  # 启动后本地数据库是否扫描过
    actor_numbers_dic: dict[str, list[str]] = field(default_factory=dict)  # 每个演员所有番号的字典
    local_number_set: set[str] = field(default_factory=set)  # 本地所有番号的集合
    local_number_cnword_set: set[str] = field(default_factory=set)  # 本地所有有字幕的番号的集合

    def reset(self) -> None:
        self.failed_list = []
        self.failed_file_list = []
        self.counting_order = 0
        self.total_count = 0
        self.rest_now_begin_count = 0
        self.sleep_end.set()  # 初始状态为未休眠
        self.scrape_starting = 0
        self.scrape_started = 0
        self.scrape_done = 0
        self.succ_count = 0
        self.fail_count = 0
        self.file_new_path_dic = {}
        self.pic_catch_set = set()
        self.file_done_dic = {}
        self.extrafanart_deal_set = set()
        self.extrafanart_copy_deal_set = set()
        self.trailer_deal_set = set()
        self.theme_videos_deal_set = set()
        self.nfo_deal_set = set()
        self.json_get_set = set()
        self.json_data_dic = {}
        self.img_path = ""


Flags = _Flags()
