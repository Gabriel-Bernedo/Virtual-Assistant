import React from 'react'

import { 
  CubeTransparentIcon as Outline_CubeTransparentIcon,
  AcademicCapIcon as Outline_AcademicCapIcon,
  PuzzlePieceIcon as Outline_PuzzlePieceIcon,
  PencilSquareIcon as Outline_PencilSquareIcon,
  CubeIcon as Outline_CubeIcon,
  QuestionMarkCircleIcon as Outline_QuestionMarkCircleIcon,
} from '@heroicons/react/24/outline'

import { 
  BookOpenIcon as Solid_BookOpenIcon,
  ChevronDownIcon as Solid_ChevronDownIcon,
} from '@heroicons/react/20/solid'

const icons = {
  outline : {
    "CubeTransparentIcon" : Outline_CubeTransparentIcon,
    "AcademicCapIcon" : Outline_AcademicCapIcon,
    "PuzzlePieceIcon" : Outline_PuzzlePieceIcon,
    "PencilSquareIcon": Outline_PencilSquareIcon,
    "CubeIcon": Outline_CubeIcon,
    "QuestionMarkCircleIcon": Outline_QuestionMarkCircleIcon,
  },
  solid : {
    "BookOpenIcon" : Solid_BookOpenIcon,
    "ChevronDownIcon": Solid_ChevronDownIcon,
  }
}

export default function MyIcon(props) {
  let MyIcon = icons[props.icon.type][props.icon.value]
  return (
    <MyIcon {...props} />
  )
}
