try:
    from fic import main
except ImportError:
    pass

try:
    from f import main
except ImportError:
    pass

if __name__ == "__main__":
    import sys
    main(sys.argv)

