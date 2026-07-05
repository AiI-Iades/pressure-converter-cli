import argparse

def convert_pressure(value, from_unit, to_unit):
    # Conversion factors (example)
    units = {
        'Pa': 1,
        'kPa': 1000,
        'bar': 100000,
        'psi': 6894.76
    }
    return value * units[to_unit] / units[from_unit]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert pressure units')
    parser.add_argument('value', type=float, help='Value to convert')
    parser.add_argument('from_unit', help='Unit to convert from')
    parser,add_argument('to_unit', help='Unit to convert to')
    args = parser.parse_args()
    result = convert_pressure(args.value, args.from_unit, args.to_unit)
    print(f'{args.value} {args.from_unit} = {result:.2f} {args.to_unit}')