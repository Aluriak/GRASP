

from operator import itemgetter
from grasp import cli
from grasp import routines


if __name__ == "__main__":

    args = cli.parse_args(__doc__)

    if args.command == 'infos':
        infos = routines.info(args.infile, args.motifs, args.no_cc,
                              graphics=args.graphics, outdir=args.outdir,
                              heavy_computations=args.heavy_computations,
                              graph_properties=args.graph_properties,
                              round_float=args.round_float,
                              negative_results=args.negative_results,
                              edge_predicate=args.edge_predicate)
        print('\n'.join(infos))
    elif args.command == 'split':
        print(routines.split_by_cc(args.infile, args.targets,
                                   edge_predicate=args.edge_predicate))
    elif args.command == 'clean':
        routines.clean(args.infile, args.target,
                       edge_predicate=args.edge_predicate,
                       target_edge_predicate=args.target_edge_predicate)
    elif args.command == 'generate':
        routines.generate(target=args.infile, method=args.method,
                          edge_predicate=args.edge_predicate)
    else:
        print('WOOT', args)