#!/usr/bin/python3
#-*- encoding: Utf-8 -*-
"""
    Note: The contents of the current file have been automatically
    generated by the "code_parsers/hermes_bytecode_structs_parser.py"
    script
    
    Please do not edit it manually. 👍
"""

from typing import List, Set, Dict, Union, Optional, Sequence, Any

# Imports from the current diretory
from def_classes import *

_instructions : List[Instructions] = []

Reg8 = OperandType('uint8_t')
Reg32 = OperandType('uint32_t')
UInt8 = OperandType('uint8_t')
UInt16 = OperandType('uint16_t')
UInt32 = OperandType('uint32_t')
Addr8 = OperandType('int8_t')
Addr32 = OperandType('int32_t')
Imm32 = OperandType('int32_t')
Double = OperandType('double')

NewObjectWithBuffer = Instruction(0, [Reg8, UInt16, UInt16, UInt16, UInt16], globals())

NewObjectWithBufferLong = Instruction(1, [Reg8, UInt16, UInt16, UInt32, UInt32], globals())

NewObject = Instruction(2, [Reg8], globals())

NewObjectWithParent = Instruction(3, [Reg8, Reg8], globals())

NewArrayWithBuffer = Instruction(4, [Reg8, UInt16, UInt16, UInt16], globals())

NewArrayWithBufferLong = Instruction(5, [Reg8, UInt16, UInt16, UInt32], globals())

NewArray = Instruction(6, [Reg8, UInt16], globals())

Mov = Instruction(7, [Reg8, Reg8], globals())

MovLong = Instruction(8, [Reg32, Reg32], globals())

Negate = Instruction(9, [Reg8, Reg8], globals())

Not = Instruction(10, [Reg8, Reg8], globals())

BitNot = Instruction(11, [Reg8, Reg8], globals())

TypeOf = Instruction(12, [Reg8, Reg8], globals())

Eq = Instruction(13, [Reg8, Reg8, Reg8], globals())

StrictEq = Instruction(14, [Reg8, Reg8, Reg8], globals())

Neq = Instruction(15, [Reg8, Reg8, Reg8], globals())

StrictNeq = Instruction(16, [Reg8, Reg8, Reg8], globals())

Less = Instruction(17, [Reg8, Reg8, Reg8], globals())

LessEq = Instruction(18, [Reg8, Reg8, Reg8], globals())

Greater = Instruction(19, [Reg8, Reg8, Reg8], globals())

GreaterEq = Instruction(20, [Reg8, Reg8, Reg8], globals())

Add = Instruction(21, [Reg8, Reg8, Reg8], globals())

AddN = Instruction(22, [Reg8, Reg8, Reg8], globals())

Mul = Instruction(23, [Reg8, Reg8, Reg8], globals())

MulN = Instruction(24, [Reg8, Reg8, Reg8], globals())

Div = Instruction(25, [Reg8, Reg8, Reg8], globals())

DivN = Instruction(26, [Reg8, Reg8, Reg8], globals())

Mod = Instruction(27, [Reg8, Reg8, Reg8], globals())

Sub = Instruction(28, [Reg8, Reg8, Reg8], globals())

SubN = Instruction(29, [Reg8, Reg8, Reg8], globals())

LShift = Instruction(30, [Reg8, Reg8, Reg8], globals())

RShift = Instruction(31, [Reg8, Reg8, Reg8], globals())

URshift = Instruction(32, [Reg8, Reg8, Reg8], globals())

BitAnd = Instruction(33, [Reg8, Reg8, Reg8], globals())

BitXor = Instruction(34, [Reg8, Reg8, Reg8], globals())

BitOr = Instruction(35, [Reg8, Reg8, Reg8], globals())

InstanceOf = Instruction(36, [Reg8, Reg8, Reg8], globals())

IsIn = Instruction(37, [Reg8, Reg8, Reg8], globals())

GetEnvironment = Instruction(38, [Reg8, UInt8], globals())

StoreToEnvironment = Instruction(39, [Reg8, UInt8, Reg8], globals())

StoreToEnvironmentL = Instruction(40, [Reg8, UInt16, Reg8], globals())

StoreNPToEnvironment = Instruction(41, [Reg8, UInt8, Reg8], globals())

StoreNPToEnvironmentL = Instruction(42, [Reg8, UInt16, Reg8], globals())

LoadFromEnvironment = Instruction(43, [Reg8, Reg8, UInt8], globals())

LoadFromEnvironmentL = Instruction(44, [Reg8, Reg8, UInt16], globals())

GetGlobalObject = Instruction(45, [Reg8], globals())

GetNewTarget = Instruction(46, [Reg8], globals())

CreateEnvironment = Instruction(47, [Reg8], globals())

DeclareGlobalVar = Instruction(48, [UInt32], globals())

DeclareGlobalVar.operands[1].operand_meaning = OperandMeaning.string_id

GetByIdShort = Instruction(49, [Reg8, Reg8, UInt8, UInt8], globals())

GetById = Instruction(50, [Reg8, Reg8, UInt8, UInt16], globals())

GetByIdLong = Instruction(51, [Reg8, Reg8, UInt8, UInt32], globals())

GetByIdShort.operands[4].operand_meaning = OperandMeaning.string_id

GetById.operands[4].operand_meaning = OperandMeaning.string_id

GetByIdLong.operands[4].operand_meaning = OperandMeaning.string_id

TryGetById = Instruction(52, [Reg8, Reg8, UInt8, UInt16], globals())

TryGetByIdLong = Instruction(53, [Reg8, Reg8, UInt8, UInt32], globals())

TryGetById.operands[4].operand_meaning = OperandMeaning.string_id

TryGetByIdLong.operands[4].operand_meaning = OperandMeaning.string_id

PutById = Instruction(54, [Reg8, Reg8, UInt8, UInt16], globals())

PutByIdLong = Instruction(55, [Reg8, Reg8, UInt8, UInt32], globals())

PutById.operands[4].operand_meaning = OperandMeaning.string_id

PutByIdLong.operands[4].operand_meaning = OperandMeaning.string_id

TryPutById = Instruction(56, [Reg8, Reg8, UInt8, UInt16], globals())

TryPutByIdLong = Instruction(57, [Reg8, Reg8, UInt8, UInt32], globals())

TryPutById.operands[4].operand_meaning = OperandMeaning.string_id

TryPutByIdLong.operands[4].operand_meaning = OperandMeaning.string_id

PutNewOwnByIdShort = Instruction(58, [Reg8, Reg8, UInt8], globals())

PutNewOwnById = Instruction(59, [Reg8, Reg8, UInt16], globals())

PutNewOwnByIdLong = Instruction(60, [Reg8, Reg8, UInt32], globals())

PutNewOwnByIdShort.operands[3].operand_meaning = OperandMeaning.string_id

PutNewOwnById.operands[3].operand_meaning = OperandMeaning.string_id

PutNewOwnByIdLong.operands[3].operand_meaning = OperandMeaning.string_id

PutNewOwnNEById = Instruction(61, [Reg8, Reg8, UInt16], globals())

PutNewOwnNEByIdLong = Instruction(62, [Reg8, Reg8, UInt32], globals())

PutNewOwnNEById.operands[3].operand_meaning = OperandMeaning.string_id

PutNewOwnNEByIdLong.operands[3].operand_meaning = OperandMeaning.string_id

PutOwnByIndex = Instruction(63, [Reg8, Reg8, UInt8], globals())

PutOwnByIndexL = Instruction(64, [Reg8, Reg8, UInt32], globals())

PutOwnByVal = Instruction(65, [Reg8, Reg8, Reg8, UInt8], globals())

DelById = Instruction(66, [Reg8, Reg8, UInt16], globals())

DelByIdLong = Instruction(67, [Reg8, Reg8, UInt32], globals())

DelById.operands[3].operand_meaning = OperandMeaning.string_id

DelByIdLong.operands[3].operand_meaning = OperandMeaning.string_id

GetByVal = Instruction(68, [Reg8, Reg8, Reg8], globals())

PutByVal = Instruction(69, [Reg8, Reg8, Reg8], globals())

DelByVal = Instruction(70, [Reg8, Reg8, Reg8], globals())

PutOwnGetterSetterByVal = Instruction(71, [Reg8, Reg8, Reg8, Reg8, UInt8], globals())

GetPNameList = Instruction(72, [Reg8, Reg8, Reg8, Reg8], globals())

GetNextPName = Instruction(73, [Reg8, Reg8, Reg8, Reg8, Reg8], globals())

Call = Instruction(74, [Reg8, Reg8, UInt8], globals())
Call.has_ret_target = True

Construct = Instruction(75, [Reg8, Reg8, UInt8], globals())
Construct.has_ret_target = True

Call1 = Instruction(76, [Reg8, Reg8, Reg8], globals())
Call1.has_ret_target = True

CallDirect = Instruction(77, [Reg8, UInt8, UInt16], globals())
CallDirect.has_ret_target = True

Call2 = Instruction(78, [Reg8, Reg8, Reg8, Reg8], globals())
Call2.has_ret_target = True

Call3 = Instruction(79, [Reg8, Reg8, Reg8, Reg8, Reg8], globals())
Call3.has_ret_target = True

Call4 = Instruction(80, [Reg8, Reg8, Reg8, Reg8, Reg8, Reg8], globals())
Call4.has_ret_target = True

CallLong = Instruction(81, [Reg8, Reg8, UInt32], globals())
CallLong.has_ret_target = True

ConstructLong = Instruction(82, [Reg8, Reg8, UInt32], globals())
ConstructLong.has_ret_target = True

CallDirectLongIndex = Instruction(83, [Reg8, UInt8, UInt32], globals())
CallDirectLongIndex.has_ret_target = True

CallBuiltin = Instruction(84, [Reg8, UInt8, UInt8], globals())

Ret = Instruction(85, [Reg8], globals())

Catch = Instruction(86, [Reg8], globals())

DirectEval = Instruction(87, [Reg8, Reg8], globals())

Throw = Instruction(88, [Reg8], globals())

Debugger = Instruction(89, [], globals())

DebuggerCheckBreak = Instruction(90, [], globals())

ProfilePoint = Instruction(91, [UInt16], globals())

Unreachable = Instruction(92, [], globals())

CreateClosure = Instruction(93, [Reg8, Reg8, UInt16], globals())

CreateClosureLongIndex = Instruction(94, [Reg8, Reg8, UInt32], globals())

CreateThis = Instruction(95, [Reg8, Reg8, Reg8], globals())

SelectObject = Instruction(96, [Reg8, Reg8, Reg8], globals())

LoadParam = Instruction(97, [Reg8, UInt8], globals())

LoadParamLong = Instruction(98, [Reg8, UInt32], globals())

LoadConstUInt8 = Instruction(99, [Reg8, UInt8], globals())

LoadConstInt = Instruction(100, [Reg8, Imm32], globals())

LoadConstDouble = Instruction(101, [Reg8, Double], globals())

LoadConstString = Instruction(102, [Reg8, UInt16], globals())

LoadConstStringLongIndex = Instruction(103, [Reg8, UInt32], globals())

LoadConstString.operands[2].operand_meaning = OperandMeaning.string_id

LoadConstStringLongIndex.operands[2].operand_meaning = OperandMeaning.string_id

LoadConstUndefined = Instruction(104, [Reg8], globals())

LoadConstNull = Instruction(105, [Reg8], globals())

LoadConstTrue = Instruction(106, [Reg8], globals())

LoadConstFalse = Instruction(107, [Reg8], globals())

LoadConstZero = Instruction(108, [Reg8], globals())

CoerceThisNS = Instruction(109, [Reg8, Reg8], globals())

LoadThisNS = Instruction(110, [Reg8], globals())

ToNumber = Instruction(111, [Reg8, Reg8], globals())

ToInt32 = Instruction(112, [Reg8, Reg8], globals())

AddEmptyString = Instruction(113, [Reg8, Reg8], globals())

GetArgumentsPropByVal = Instruction(114, [Reg8, Reg8, Reg8], globals())

GetArgumentsLength = Instruction(115, [Reg8, Reg8], globals())

ReifyArguments = Instruction(116, [Reg8], globals())

CreateRegExp = Instruction(117, [Reg8, UInt32, UInt32, UInt32], globals())

CreateRegExp.operands[2].operand_meaning = OperandMeaning.string_id

CreateRegExp.operands[3].operand_meaning = OperandMeaning.string_id

SwitchImm = Instruction(118, [Reg8, UInt32, Addr32, UInt32, UInt32], globals())

Jmp = Operand(119, [Addr8], globals())
JmpLong = Operand(120, [Addr32], globals())

JmpTrue = Operand(121, [Addr8, Reg8], globals())
JmpTrueLong = Operand(122, [Addr32, Reg8], globals())

JmpFalse = Operand(123, [Addr8, Reg8], globals())
JmpFalseLong = Operand(124, [Addr32, Reg8], globals())

JmpUndefined = Operand(125, [Addr8, Reg8], globals())
JmpUndefinedLong = Operand(126, [Addr32, Reg8], globals())

JLess = Operand(127, [Addr8, Reg8, Reg8], globals())
JLessLong = Operand(128, [Addr32, Reg8, Reg8], globals())

JNotLess = Operand(129, [Addr8, Reg8, Reg8], globals())
JNotLessLong = Operand(130, [Addr32, Reg8, Reg8], globals())

JLessN = Operand(131, [Addr8, Reg8, Reg8], globals())
JLessNLong = Operand(132, [Addr32, Reg8, Reg8], globals())

JNotLessN = Operand(133, [Addr8, Reg8, Reg8], globals())
JNotLessNLong = Operand(134, [Addr32, Reg8, Reg8], globals())

JLessEqual = Operand(135, [Addr8, Reg8, Reg8], globals())
JLessEqualLong = Operand(136, [Addr32, Reg8, Reg8], globals())

JNotLessEqual = Operand(137, [Addr8, Reg8, Reg8], globals())
JNotLessEqualLong = Operand(138, [Addr32, Reg8, Reg8], globals())

JLessEqualN = Operand(139, [Addr8, Reg8, Reg8], globals())
JLessEqualNLong = Operand(140, [Addr32, Reg8, Reg8], globals())

JNotLessEqualN = Operand(141, [Addr8, Reg8, Reg8], globals())
JNotLessEqualNLong = Operand(142, [Addr32, Reg8, Reg8], globals())

JGreater = Operand(143, [Addr8, Reg8, Reg8], globals())
JGreaterLong = Operand(144, [Addr32, Reg8, Reg8], globals())

JNotGreater = Operand(145, [Addr8, Reg8, Reg8], globals())
JNotGreaterLong = Operand(146, [Addr32, Reg8, Reg8], globals())

JGreaterN = Operand(147, [Addr8, Reg8, Reg8], globals())
JGreaterNLong = Operand(148, [Addr32, Reg8, Reg8], globals())

JNotGreaterN = Operand(149, [Addr8, Reg8, Reg8], globals())
JNotGreaterNLong = Operand(150, [Addr32, Reg8, Reg8], globals())

JGreaterEqual = Operand(151, [Addr8, Reg8, Reg8], globals())
JGreaterEqualLong = Operand(152, [Addr32, Reg8, Reg8], globals())

JNotGreaterEqual = Operand(153, [Addr8, Reg8, Reg8], globals())
JNotGreaterEqualLong = Operand(154, [Addr32, Reg8, Reg8], globals())

JGreaterEqualN = Operand(155, [Addr8, Reg8, Reg8], globals())
JGreaterEqualNLong = Operand(156, [Addr32, Reg8, Reg8], globals())

JNotGreaterEqualN = Operand(157, [Addr8, Reg8, Reg8], globals())
JNotGreaterEqualNLong = Operand(158, [Addr32, Reg8, Reg8], globals())

JEqual = Operand(159, [Addr8, Reg8, Reg8], globals())
JEqualLong = Operand(160, [Addr32, Reg8, Reg8], globals())

JNotEqual = Operand(161, [Addr8, Reg8, Reg8], globals())
JNotEqualLong = Operand(162, [Addr32, Reg8, Reg8], globals())

JStrictEqual = Operand(163, [Addr8, Reg8, Reg8], globals())
JStrictEqualLong = Operand(164, [Addr32, Reg8, Reg8], globals())

JStrictNotEqual = Operand(165, [Addr8, Reg8, Reg8], globals())
JStrictNotEqualLong = Operand(166, [Addr32, Reg8, Reg8], globals())

_opcode_to_instruction : Dict[int, Instruction] = {v.opcode: v for v in _instructions}
_name_to_instruction : Dict[str, Instruction] = {v.name: v for v in _instructions}

