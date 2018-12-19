#!/bin/bash
function submit 			{ leetcode submit $2;} 
function sortedEasyAll 		{ leetcode list -q eL | awk '{print substr($(NF-1), 2), $0}' | sort -g ; }
function sortedEasyUndone 	{ leetcode list -q eDL | awk '{print substr($(NF-1), 2), $0}' | sort -g ; }
function sortedMediumAll 	{ leetcode list -q mL | awk '{print substr($(NF-1), 2), $0}' | sort -g ; }
function sortedMediumUndone { leetcode list -q mLD | awk '{print substr($(NF-1), 2), $0}' | sort -g ; }

function usage {
	echo -e "Usage:
	-s 	submit a new solution
	-e 	list all easy (unlocked) questions, 
	-eu 	list all undone easy (unlocked) questions 	
	-m 	list all medium (unlocked) questions 
	-mu 	list all undone medium (unlocked) questions (sorted by the accepted ratio)
	"
}

if [ $# -eq 0 ]; then
	usage
	exit
fi

case $1 in
	'-e')  sortedEasyAll;;
	'-eu') sortedEasyUndone;;
	'-m')  sortedMediumAll;;
	'-mu') sortedMediumUndone;;
	'-s')  submit;;
	*)	   usage;;
esac
