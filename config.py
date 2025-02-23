import argparse
import os

"""
Detailed hyper-parameter configurations.
"""


def all_param(parser: argparse.ArgumentParser):
    # common parameters
    parser.add_argument("--gpu", default=0, type=int)

    parser.add_argument("--data_name", default='FewRel', type=str, help="Use TACRED or FewRel datasets.")

    parser.add_argument("--task_name", default='FewRel', type=str)

    parser.add_argument("--max_length", default=256, type=int)

    parser.add_argument("--this_name", default="continual", type=str)

    parser.add_argument("--device", default="cuda", type=str)

    # training parameters

    parser.add_argument("--batch_size", default=16, type=int)

    parser.add_argument("--learning_rate", default=5e-6, type=float)

    parser.add_argument("--total_round", default=5, type=int)

    parser.add_argument("--rel_per_task", default=4)

    parser.add_argument("--pattern", default="entity_marker")

    parser.add_argument("--encoder_output_size", default=768, type=int)

    parser.add_argument("--vocab_size", default=30522, type=int)

    parser.add_argument("--marker_size", default=4, type=int)

    # Temperature parameter in CL and CR
    parser.add_argument("--temp", default=0.1, type=float)

    # The projection head outputs dimensions
    parser.add_argument("--feat_dim", default=64, type=int)

    # Temperature parameter in KL
    parser.add_argument("--kl_temp", default=10, type=float)

    parser.add_argument("--num_workers", default=0, type=int)

    # epoch1
    parser.add_argument("--step1_epochs", default=10, type=int)

    # epoch2
    parser.add_argument("--step2_epochs", default=10, type=int)

    parser.add_argument("--seed", default=2021, type=int)

    parser.add_argument("--max_grad_norm", default=10, type=float)

    # Memory size
    parser.add_argument("--num_protos", default=20, type=int)

    parser.add_argument("--optim", default='adam', type=str)

    # dataset path
    parser.add_argument("--data_path", default='dataset/', type=str)

    # bert-base-uncased weights path
    parser.add_argument("--bert_path", default="H:\\2024-winter\\relationship\\realtionship-code\\bert-base-uncased", type=str)

    # Data Augmentation
    parser.add_argument("--data_augmentation", default=False, type=bool)

    # result path
    parser.add_argument("--result_path", default="result", type=str)

    return parser


class Param:

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser = all_param(self.parser)

    def get_args(self):
        all_args, unknown = self.parser.parse_known_args()
        return all_args
