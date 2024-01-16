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
import Kanban from './Kanban'
import Inbox from './Inbox'
import Products from './Products'
import SignIn from './SignIn'
import SignUp from './SignUp'
import Users from './Users'
import Save from './Save'
import Delete from './Delete'
import Add from './Add'
import DownArrow from './DownArrow'
import ShoppingCar from './ShoppingCar'

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
  },
  original: {
    "Kanban": Kanban,
    "Inbox": Inbox,
    "Products": Products,
    "SignIn": SignIn,
    "SignUp": SignUp,
    "Users": Users,
    "DownArrow" : DownArrow,
    "ShoppingCar": ShoppingCar,
  },
  options: {
    "Save": Save,
    "Delete": Delete,
    "Add": Add,
  }
}

export default function MyIcon(props) {
  let MyIcon = icons[props.icon.type][props.icon.value]
  return (
    <MyIcon {...props} />
  )
}

