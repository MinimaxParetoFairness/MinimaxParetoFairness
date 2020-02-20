import argparse
import torch


class Config:
    def __init__(self):
        self.parser = argparse.ArgumentParser()

    def add_argument(self, *args, **kwargs):
        self.parser.add_argument(*args, **kwargs)

    def merge(self,argv, config_dict=None ):
        if config_dict is None:
            # args = self.parser.parse_args(argv)
            args, unknown = self.parser.parse_known_args(argv)
            config_dict = args.__dict__
        for key in config_dict.keys():
            setattr(self, key, config_dict[key])

# def make_defconfig():
#     # Make config
#     config = Config()
#
#     # Basic configuration
#     config.add_argument('--bs', action='store', default=0, type=int, dest='BATCH_SIZE', help='batch size')
#     config.add_argument('--epochs', action='store', default=1000, type=int, dest='EPOCHS',
#                         help='maximum number of epochs')
#     config.add_argument('--lr', action='store', default=0, type=float, dest='LEARNING_RATE', help='learning rate')
#     config.add_argument('--momentum', action='store', default=0.9, type=float, dest='MOMENTUM',
#                         help='nesterov momentum')
#     config.add_argument('--gpu_id', action='store', default=0, type=int, dest='GPU_ID',
#                         help='gpu id, use -1 to run on cpu')
#     config.add_argument('--n_workers', action='store', default=32, type=int, dest='n_dataloader',
#                         help='number of dataloader parallel workers')
#     config.add_argument('--seed', action='store', default=42, type=int, dest='seed', help='randomizer seed')
#     config.add_argument('--dataset', action='store', default='adult_race_gender', type=str, dest='dataset',
#                         help='dataset name')
#     config.add_argument('--split', action='store', default=0, type=int, dest='split', help='dataset split number')
#     config.add_argument('--lrdecay', action='store', default=0.25, type=float, dest='lrdecay',
#                         help='learning rate decay')
#     config.add_argument('--optimizer', type=str, default='adam', help='optimizer to use (sgd, adam)')
#     config.add_argument('--prefix', action='store', default='', type=str, dest='prefix', help='save file prefix')
#
#     config.add_argument('--shl', action='store', default='', type=str, dest='shidden', help='size of hidden layers')
#
#     # Print, log and store options
#     config.add_argument('--verbose', action='store', default=True, type=lambda x: bool(strtobool(x)),
#                         help='boolean: print updates?')
#     config.add_argument('--n_print', action='store', default=5, type=int, dest='n_print', help='print frequency')
#     config.add_argument('--log', action='store', default=False, type=lambda x: bool(strtobool(x)), dest='logger_active',
#                         help='boolean: create tensorboard log?')
#
#     # Pareto-optimality options
#     config.add_argument('--patience', action='store', default=20, type=int, dest='patience',
#                         help='epoch patience parameter inside adaptive optimization')
#     config.add_argument('--mu_init', action='store', default='', type=str, dest='mu_init', help='initial mu penalty')
#     config.add_argument('--loss_type', action='store', default=0, type=int, dest='type_loss',
#                         help='0: CrossEntropy, 1: Total Variation 2:Brier score (Categorical MSE)')
#     config.add_argument('--sampler', action='store', default=True, type=lambda x: bool(strtobool(x)), dest='sampler',
#                         help='boolean: activate discrimination penalty')
#     config.add_argument('--type', type=str, default='minimax', help='type of fit (minimax, balanced , naive)')
#     config.add_argument('--niter', action='store', default=0, type=int, dest='niter_apstar',
#                         help='niterations for APSTAR')
#
#     argv = sys.argv
#     config.merge(argv)
#
#     return config