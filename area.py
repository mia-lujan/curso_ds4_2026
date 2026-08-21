"""Calculate the area of a rectangle given its lenght and width"""
import argparse

def calculate_rectangle_area(length, width):
    """calculate the area of a rectangle."""

    return length * width
def main():
    parser = argparse.ArgumentParser(
        description="Calculate the area of a rectangle given its length and width.")
    parser.add_argument("length", type=float, help="Length of the rectangle")
    parser.add_argument("width", type=float, help="Width of the rectangle")
    help= ""
    args = parser.parse_args()

    area = calculate_rectangle_area(args.length, args.width)
    print(f"The area of the rectangle is: {area}")

if __name__ == "__main__":
    main()

"""aaaaaaaaaaaaaaaaaaaaaaaa"""