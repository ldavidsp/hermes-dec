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

Unreachable = Instruction(0, [], globals())

NewObjectWithBuffer = Instruction(1, [Reg8, UInt16, UInt16, UInt16, UInt16], globals())

NewObjectWithBufferLong = Instruction(2, [Reg8, UInt16, UInt16, UInt32, UInt32], globals())

NewObject = Instruction(3, [Reg8], globals())

NewObjectWithParent = Instruction(4, [Reg8, Reg8], globals())

NewArrayWithBuffer = Instruction(5, [Reg8, UInt16, UInt16, UInt16], globals())

NewArrayWithBufferLong = Instruction(6, [Reg8, UInt16, UInt16, UInt32], globals())

NewArray = Instruction(7, [Reg8, UInt16], globals())

Mov = Instruction(8, [Reg8, Reg8], globals())

MovLong = Instruction(9, [Reg32, Reg32], globals())

Negate = Instruction(10, [Reg8, Reg8], globals())

Not = Instruction(11, [Reg8, Reg8], globals())

BitNot = Instruction(12, [Reg8, Reg8], globals())

TypeOf = Instruction(13, [Reg8, Reg8], globals())

Eq = Instruction(14, [Reg8, Reg8, Reg8], globals())

StrictEq = Instruction(15, [Reg8, Reg8, Reg8], globals())

Neq = Instruction(16, [Reg8, Reg8, Reg8], globals())

StrictNeq = Instruction(17, [Reg8, Reg8, Reg8], globals())

Less = Instruction(18, [Reg8, Reg8, Reg8], globals())

LessEq = Instruction(19, [Reg8, Reg8, Reg8], globals())

Greater = Instruction(20, [Reg8, Reg8, Reg8], globals())

GreaterEq = Instruction(21, [Reg8, Reg8, Reg8], globals())

Add = Instruction(22, [Reg8, Reg8, Reg8], globals())

AddN = Instruction(23, [Reg8, Reg8, Reg8], globals())

Mul = Instruction(24, [Reg8, Reg8, Reg8], globals())

MulN = Instruction(25, [Reg8, Reg8, Reg8], globals())

Div = Instruction(26, [Reg8, Reg8, Reg8], globals())

DivN = Instruction(27, [Reg8, Reg8, Reg8], globals())

Mod = Instruction(28, [Reg8, Reg8, Reg8], globals())

Sub = Instruction(29, [Reg8, Reg8, Reg8], globals())

SubN = Instruction(30, [Reg8, Reg8, Reg8], globals())

LShift = Instruction(31, [Reg8, Reg8, Reg8], globals())

RShift = Instruction(32, [Reg8, Reg8, Reg8], globals())

URshift = Instruction(33, [Reg8, Reg8, Reg8], globals())

BitAnd = Instruction(34, [Reg8, Reg8, Reg8], globals())

BitXor = Instruction(35, [Reg8, Reg8, Reg8], globals())

BitOr = Instruction(36, [Reg8, Reg8, Reg8], globals())

InstanceOf = Instruction(37, [Reg8, Reg8, Reg8], globals())

IsIn = Instruction(38, [Reg8, Reg8, Reg8], globals())

GetEnvironment = Instruction(39, [Reg8, UInt8], globals())

StoreToEnvironment = Instruction(40, [Reg8, UInt8, Reg8], globals())

StoreToEnvironmentL = Instruction(41, [Reg8, UInt16, Reg8], globals())

StoreNPToEnvironment = Instruction(42, [Reg8, UInt8, Reg8], globals())

StoreNPToEnvironmentL = Instruction(43, [Reg8, UInt16, Reg8], globals())

LoadFromEnvironment = Instruction(44, [Reg8, Reg8, UInt8], globals())

LoadFromEnvironmentL = Instruction(45, [Reg8, Reg8, UInt16], globals())

GetGlobalObject = Instruction(46, [Reg8], globals())

GetNewTarget = Instruction(47, [Reg8], globals())

CreateEnvironment = Instruction(48, [Reg8], globals())

DeclareGlobalVar = Instruction(49, [UInt32], globals())

DeclareGlobalVar.operands[1].operand_meaning = OperandMeaning.string_id

GetByIdShort = Instruction(50, [Reg8, Reg8, UInt8, UInt8], globals())

GetById = Instruction(51, [Reg8, Reg8, UInt8, UInt16], globals())

GetByIdLong = Instruction(52, [Reg8, Reg8, UInt8, UInt32], globals())

GetByIdShort.operands[4].operand_meaning = OperandMeaning.string_id

GetById.operands[4].operand_meaning = OperandMeaning.string_id

GetByIdLong.operands[4].operand_meaning = OperandMeaning.string_id

TryGetById = Instruction(53, [Reg8, Reg8, UInt8, UInt16], globals())

TryGetByIdLong = Instruction(54, [Reg8, Reg8, UInt8, UInt32], globals())

TryGetById.operands[4].operand_meaning = OperandMeaning.string_id

TryGetByIdLong.operands[4].operand_meaning = OperandMeaning.string_id

PutById = Instruction(55, [Reg8, Reg8, UInt8, UInt16], globals())

PutByIdLong = Instruction(56, [Reg8, Reg8, UInt8, UInt32], globals())

PutById.operands[4].operand_meaning = OperandMeaning.string_id

PutByIdLong.operands[4].operand_meaning = OperandMeaning.string_id

TryPutById = Instruction(57, [Reg8, Reg8, UInt8, UInt16], globals())

TryPutByIdLong = Instruction(58, [Reg8, Reg8, UInt8, UInt32], globals())

TryPutById.operands[4].operand_meaning = OperandMeaning.string_id

TryPutByIdLong.operands[4].operand_meaning = OperandMeaning.string_id

PutNewOwnByIdShort = Instruction(59, [Reg8, Reg8, UInt8], globals())

PutNewOwnById = Instruction(60, [Reg8, Reg8, UInt16], globals())

PutNewOwnByIdLong = Instruction(61, [Reg8, Reg8, UInt32], globals())

PutNewOwnByIdShort.operands[3].operand_meaning = OperandMeaning.string_id

PutNewOwnById.operands[3].operand_meaning = OperandMeaning.string_id

PutNewOwnByIdLong.operands[3].operand_meaning = OperandMeaning.string_id

PutNewOwnNEById = Instruction(62, [Reg8, Reg8, UInt16], globals())

PutNewOwnNEByIdLong = Instruction(63, [Reg8, Reg8, UInt32], globals())

PutNewOwnNEById.operands[3].operand_meaning = OperandMeaning.string_id

PutNewOwnNEByIdLong.operands[3].operand_meaning = OperandMeaning.string_id

PutOwnByIndex = Instruction(64, [Reg8, Reg8, UInt8], globals())

PutOwnByIndexL = Instruction(65, [Reg8, Reg8, UInt32], globals())

PutOwnByVal = Instruction(66, [Reg8, Reg8, Reg8, UInt8], globals())

DelById = Instruction(67, [Reg8, Reg8, UInt16], globals())

DelByIdLong = Instruction(68, [Reg8, Reg8, UInt32], globals())

DelById.operands[3].operand_meaning = OperandMeaning.string_id

DelByIdLong.operands[3].operand_meaning = OperandMeaning.string_id

GetByVal = Instruction(69, [Reg8, Reg8, Reg8], globals())

PutByVal = Instruction(70, [Reg8, Reg8, Reg8], globals())

DelByVal = Instruction(71, [Reg8, Reg8, Reg8], globals())

PutOwnGetterSetterByVal = Instruction(72, [Reg8, Reg8, Reg8, Reg8, UInt8], globals())

GetPNameList = Instruction(73, [Reg8, Reg8, Reg8, Reg8], globals())

GetNextPName = Instruction(74, [Reg8, Reg8, Reg8, Reg8, Reg8], globals())

Call = Instruction(75, [Reg8, Reg8, UInt8], globals())
Call.has_ret_target = True

Construct = Instruction(76, [Reg8, Reg8, UInt8], globals())
Construct.has_ret_target = True

Call1 = Instruction(77, [Reg8, Reg8, Reg8], globals())
Call1.has_ret_target = True

CallDirect = Instruction(78, [Reg8, UInt8, UInt16], globals())
CallDirect.has_ret_target = True

Call2 = Instruction(79, [Reg8, Reg8, Reg8, Reg8], globals())
Call2.has_ret_target = True

Call3 = Instruction(80, [Reg8, Reg8, Reg8, Reg8, Reg8], globals())
Call3.has_ret_target = True

Call4 = Instruction(81, [Reg8, Reg8, Reg8, Reg8, Reg8, Reg8], globals())
Call4.has_ret_target = True

CallLong = Instruction(82, [Reg8, Reg8, UInt32], globals())
CallLong.has_ret_target = True

ConstructLong = Instruction(83, [Reg8, Reg8, UInt32], globals())
ConstructLong.has_ret_target = True

CallDirectLongIndex = Instruction(84, [Reg8, UInt8, UInt32], globals())
CallDirectLongIndex.has_ret_target = True

CallBuiltin = Instruction(85, [Reg8, UInt8, UInt8], globals())

CallBuiltinLong = Instruction(86, [Reg8, UInt8, UInt32], globals())

GetBuiltinClosure = Instruction(87, [Reg8, UInt8], globals())

Ret = Instruction(88, [Reg8], globals())

Catch = Instruction(89, [Reg8], globals())

DirectEval = Instruction(90, [Reg8, Reg8], globals())

Throw = Instruction(91, [Reg8], globals())

ThrowIfEmpty = Instruction(92, [Reg8, Reg8], globals())

Debugger = Instruction(93, [], globals())

AsyncBreakCheck = Instruction(94, [], globals())

ProfilePoint = Instruction(95, [UInt16], globals())

CreateClosure = Instruction(96, [Reg8, Reg8, UInt16], globals())

CreateClosureLongIndex = Instruction(97, [Reg8, Reg8, UInt32], globals())

CreateGeneratorClosure = Instruction(98, [Reg8, Reg8, UInt16], globals())

CreateGeneratorClosureLongIndex = Instruction(99, [Reg8, Reg8, UInt32], globals())

CreateAsyncClosure = Instruction(100, [Reg8, Reg8, UInt16], globals())

CreateAsyncClosureLongIndex = Instruction(101, [Reg8, Reg8, UInt32], globals())

CreateThis = Instruction(102, [Reg8, Reg8, Reg8], globals())

SelectObject = Instruction(103, [Reg8, Reg8, Reg8], globals())

LoadParam = Instruction(104, [Reg8, UInt8], globals())

LoadParamLong = Instruction(105, [Reg8, UInt32], globals())

LoadConstUInt8 = Instruction(106, [Reg8, UInt8], globals())

LoadConstInt = Instruction(107, [Reg8, Imm32], globals())

LoadConstDouble = Instruction(108, [Reg8, Double], globals())

LoadConstString = Instruction(109, [Reg8, UInt16], globals())

LoadConstStringLongIndex = Instruction(110, [Reg8, UInt32], globals())

LoadConstString.operands[2].operand_meaning = OperandMeaning.string_id

LoadConstStringLongIndex.operands[2].operand_meaning = OperandMeaning.string_id

LoadConstEmpty = Instruction(111, [Reg8], globals())

LoadConstUndefined = Instruction(112, [Reg8], globals())

LoadConstNull = Instruction(113, [Reg8], globals())

LoadConstTrue = Instruction(114, [Reg8], globals())

LoadConstFalse = Instruction(115, [Reg8], globals())

LoadConstZero = Instruction(116, [Reg8], globals())

CoerceThisNS = Instruction(117, [Reg8, Reg8], globals())

LoadThisNS = Instruction(118, [Reg8], globals())

ToNumber = Instruction(119, [Reg8, Reg8], globals())

ToInt32 = Instruction(120, [Reg8, Reg8], globals())

AddEmptyString = Instruction(121, [Reg8, Reg8], globals())

GetArgumentsPropByVal = Instruction(122, [Reg8, Reg8, Reg8], globals())

GetArgumentsLength = Instruction(123, [Reg8, Reg8], globals())

ReifyArguments = Instruction(124, [Reg8], globals())

CreateRegExp = Instruction(125, [Reg8, UInt32, UInt32, UInt32], globals())

CreateRegExp.operands[2].operand_meaning = OperandMeaning.string_id

CreateRegExp.operands[3].operand_meaning = OperandMeaning.string_id

SwitchImm = Instruction(126, [Reg8, UInt32, Addr32, UInt32, UInt32], globals())

StartGenerator = Instruction(127, [], globals())

ResumeGenerator = Instruction(128, [Reg8, Reg8], globals())

CompleteGenerator = Instruction(129, [], globals())

CreateGenerator = Instruction(130, [Reg8, Reg8, UInt16], globals())

CreateGeneratorLongIndex = Instruction(131, [Reg8, Reg8, UInt32], globals())

IteratorBegin = Instruction(132, [Reg8, Reg8], globals())

IteratorNext = Instruction(133, [Reg8, Reg8, Reg8], globals())

IteratorClose = Instruction(134, [Reg8, UInt8], globals())

Jmp = Operand(135, [Addr8], globals())
JmpLong = Operand(136, [Addr32], globals())

JmpTrue = Operand(137, [Addr8, Reg8], globals())
JmpTrueLong = Operand(138, [Addr32, Reg8], globals())

JmpFalse = Operand(139, [Addr8, Reg8], globals())
JmpFalseLong = Operand(140, [Addr32, Reg8], globals())

JmpUndefined = Operand(141, [Addr8, Reg8], globals())
JmpUndefinedLong = Operand(142, [Addr32, Reg8], globals())

SaveGenerator = Operand(143, [Addr8], globals())
SaveGeneratorLong = Operand(144, [Addr32], globals())

JLess = Operand(145, [Addr8, Reg8, Reg8], globals())
JLessLong = Operand(146, [Addr32, Reg8, Reg8], globals())

JNotLess = Operand(147, [Addr8, Reg8, Reg8], globals())
JNotLessLong = Operand(148, [Addr32, Reg8, Reg8], globals())

JLessN = Operand(149, [Addr8, Reg8, Reg8], globals())
JLessNLong = Operand(150, [Addr32, Reg8, Reg8], globals())

JNotLessN = Operand(151, [Addr8, Reg8, Reg8], globals())
JNotLessNLong = Operand(152, [Addr32, Reg8, Reg8], globals())

JLessEqual = Operand(153, [Addr8, Reg8, Reg8], globals())
JLessEqualLong = Operand(154, [Addr32, Reg8, Reg8], globals())

JNotLessEqual = Operand(155, [Addr8, Reg8, Reg8], globals())
JNotLessEqualLong = Operand(156, [Addr32, Reg8, Reg8], globals())

JLessEqualN = Operand(157, [Addr8, Reg8, Reg8], globals())
JLessEqualNLong = Operand(158, [Addr32, Reg8, Reg8], globals())

JNotLessEqualN = Operand(159, [Addr8, Reg8, Reg8], globals())
JNotLessEqualNLong = Operand(160, [Addr32, Reg8, Reg8], globals())

JGreater = Operand(161, [Addr8, Reg8, Reg8], globals())
JGreaterLong = Operand(162, [Addr32, Reg8, Reg8], globals())

JNotGreater = Operand(163, [Addr8, Reg8, Reg8], globals())
JNotGreaterLong = Operand(164, [Addr32, Reg8, Reg8], globals())

JGreaterN = Operand(165, [Addr8, Reg8, Reg8], globals())
JGreaterNLong = Operand(166, [Addr32, Reg8, Reg8], globals())

JNotGreaterN = Operand(167, [Addr8, Reg8, Reg8], globals())
JNotGreaterNLong = Operand(168, [Addr32, Reg8, Reg8], globals())

JGreaterEqual = Operand(169, [Addr8, Reg8, Reg8], globals())
JGreaterEqualLong = Operand(170, [Addr32, Reg8, Reg8], globals())

JNotGreaterEqual = Operand(171, [Addr8, Reg8, Reg8], globals())
JNotGreaterEqualLong = Operand(172, [Addr32, Reg8, Reg8], globals())

JGreaterEqualN = Operand(173, [Addr8, Reg8, Reg8], globals())
JGreaterEqualNLong = Operand(174, [Addr32, Reg8, Reg8], globals())

JNotGreaterEqualN = Operand(175, [Addr8, Reg8, Reg8], globals())
JNotGreaterEqualNLong = Operand(176, [Addr32, Reg8, Reg8], globals())

JEqual = Operand(177, [Addr8, Reg8, Reg8], globals())
JEqualLong = Operand(178, [Addr32, Reg8, Reg8], globals())

JNotEqual = Operand(179, [Addr8, Reg8, Reg8], globals())
JNotEqualLong = Operand(180, [Addr32, Reg8, Reg8], globals())

JStrictEqual = Operand(181, [Addr8, Reg8, Reg8], globals())
JStrictEqualLong = Operand(182, [Addr32, Reg8, Reg8], globals())

JStrictNotEqual = Operand(183, [Addr8, Reg8, Reg8], globals())
JStrictNotEqualLong = Operand(184, [Addr32, Reg8, Reg8], globals())

_opcode_to_instruction : Dict[int, Instruction] = {v.opcode: v for v in _instructions}
_name_to_instruction : Dict[str, Instruction] = {v.name: v for v in _instructions}

