import sys
import pstats
import logging
import cProfile
import problem1 as p1
import problem2 as p2
import problem3 as p3
import problem4 as p4
import problem5 as p5
import problem6 as p6
import problem7 as p7
import problem8 as p8
import problem9 as p9
import problem10 as p10
import problem11 as p11

def main():
	logging.basicConfig(level=logging.DEBUG, format="[%(levelname)s] %(asctime)s - %(message)s")
	if len(sys.argv) < 2: 
		logging.error("Please provide a problem number")
		return
	problem_number = int(sys.argv[1])
	with cProfile.Profile() as pr:
		if   problem_number == 1:	p1.main()
		elif problem_number == 2:	p2.main()
		elif problem_number == 3:	p3.main()
		elif problem_number == 4:	p4.main()
		elif problem_number == 5:	p5.main()
		elif problem_number == 6:	p6.main()
		elif problem_number == 7:	p7.main()
		elif problem_number == 8:	p8.main()
		elif problem_number == 9:	p9.main()
		elif problem_number == 10:	p10.main()
		elif problem_number == 11:	p11.main()
		else: logging.error("Please provide a valid number")
	stats = pstats.Stats(pr)
	stats.sort_stats(pstats.SortKey.TIME)
	# stats.print_stats()
if __name__ == '__main__': main()
