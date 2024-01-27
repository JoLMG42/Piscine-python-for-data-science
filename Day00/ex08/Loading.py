import time
import os


def ft_tqdm(lst: range) -> None:
    """
        This function print a progress bar,
        with lst.stop for number of iterations
    """
    start = time.time()
    estim = lst.stop / 98
    c = os.get_terminal_size().columns - 35
    for k in lst:
        yield k
        actu = time.time()
        diff = actu - start
        freq = k / diff
        percentage = int((k / lst.stop) * 100)
        progress = int((int(c) * k) / lst.stop)
        bar1 = "{}%|{:{len}}| ".format(percentage + 1, progress*'█', len=c - 1)
        bar2 = "{}/{} [{:.1f}-{:.1f}".format(k + 1, lst.stop, diff, estim)
        bar = "{}{}, {:.2f}it/s]".format(bar1, bar2, freq)
        print(bar, end="\r")
        estim = (lst.stop - k) / freq if freq > 0 else 0
