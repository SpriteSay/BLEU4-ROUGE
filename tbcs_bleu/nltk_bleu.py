from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
import ipdb

smoothing0 = SmoothingFunction().method0
smoothing1 = SmoothingFunction().method1
smoothing2 = SmoothingFunction().method2
smoothing3 = SmoothingFunction().method3
smoothing4 = SmoothingFunction().method4
smoothing5 = SmoothingFunction().method5
smoothing6 = SmoothingFunction().method6

def nltk_sentence_bleu_innner(hypotheses, references, smooth_func, smooth_id):
    total_score = 0
    count = len(hypotheses)
    for Id in list(hypotheses.keys()):
        hyp = hypotheses[Id][0].split()
        ref = [r.split() for r in references[Id]]
        score = sentence_bleu(ref, hyp, weights=(0.25, 0.25, 0.25, 0.25), smoothing_function=smooth_func)
        total_score += score
    avg_score = total_score / count
    print(f'sooth with {smooth_id} and score: {avg_score}')
    return avg_score

def nltk_sentence_bleu(hypotheses, references):
    idx = 0
    for smooth_func in [smoothing0, smoothing1, smoothing2, smoothing3, smoothing4, smoothing5]:
        idx += 1
        nltk_sentence_bleu_innner(hypotheses, references, smooth_func, idx)