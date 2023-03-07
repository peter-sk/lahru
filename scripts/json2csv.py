#!/usr/bin/env python
from csv import writer
from json import load
from sys import argv, stdin, stdout
class ns:
    def __init__(self, d):
        [setattr(self, n, d[n]) for n in d]
h = load(stdin)['log_history']
w = writer(stdout)
w.writerow("step,epoch,loss,eval_loss,learning_rate".split(","))
while h:
    t, e, h = ns(h[0]), ns(h[1]), h[2:]
    w.writerow((t.step, t.epoch, t.loss, e.eval_loss, t.learning_rate))
