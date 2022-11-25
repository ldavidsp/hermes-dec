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
from .def_classes import *

_instructions : List[Instruction] = []

Reg8 = OperandType('Reg8', 'uint8_t')
Reg32 = OperandType('Reg32', 'uint32_t')
UInt8 = OperandType('UInt8', 'uint8_t')
UInt16 = OperandType('UInt16', 'uint16_t')
UInt32 = OperandType('UInt32', 'uint32_t')
Addr8 = OperandType('Addr8', 'int8_t')
Addr32 = OperandType('Addr32', 'int32_t')
Imm32 = OperandType('Imm32', 'int32_t')
Double = OperandType('Double', 'double')

Unreachable = Instruction('Unreachable', 0, [], globals())

NewObjectWithBuffer = Instruction('NewObjectWithBuffer', 1, [Reg8, UInt16, UInt16, UInt16, UInt16], globals())

NewObjectWithBufferLong = Instruction('NewObjectWithBufferLong', 2, [Reg8, UInt16, UInt16, UInt32, UInt32], globals())

NewObject = Instruction('NewObject', 3, [Reg8], globals())

NewObjectWithParent = Instruction('NewObjectWithParent', 4, [Reg8, Reg8], globals())

NewArrayWithBuffer = Instruction('NewArrayWithBuffer', 5, [Reg8, UInt16, UInt16, UInt16], globals())

NewArrayWithBufferLong = Instruction('NewArrayWithBufferLong', 6, [Reg8, UInt16, UInt16, UInt32], globals())

NewArray = Instruction('NewArray', 7, [Reg8, UInt16], globals())

Mov = Instruction('Mov', 8, [Reg8, Reg8], globals())

MovLong = Instruction('MovLong', 9, [Reg32, Reg32], globals())

Negate = Instruction('Negate', 10, [Reg8, Reg8], globals())

Not = Instruction('Not', 11, [Reg8, Reg8], globals())

BitNot = Instruction('BitNot', 12, [Reg8, Reg8], globals())

TypeOf = Instruction('TypeOf', 13, [Reg8, Reg8], globals())

Eq = Instruction('Eq', 14, [Reg8, Reg8, Reg8], globals())

StrictEq = Instruction('StrictEq', 15, [Reg8, Reg8, Reg8], globals())

Neq = Instruction('Neq', 16, [Reg8, Reg8, Reg8], globals())

StrictNeq = Instruction('StrictNeq', 17, [Reg8, Reg8, Reg8], globals())

Less = Instruction('Less', 18, [Reg8, Reg8, Reg8], globals())

LessEq = Instruction('LessEq', 19, [Reg8, Reg8, Reg8], globals())

Greater = Instruction('Greater', 20, [Reg8, Reg8, Reg8], globals())

GreaterEq = Instruction('GreaterEq', 21, [Reg8, Reg8, Reg8], globals())

Add = Instruction('Add', 22, [Reg8, Reg8, Reg8], globals())

AddN = Instruction('AddN', 23, [Reg8, Reg8, Reg8], globals())

Mul = Instruction('Mul', 24, [Reg8, Reg8, Reg8], globals())

MulN = Instruction('MulN', 25, [Reg8, Reg8, Reg8], globals())

Div = Instruction('Div', 26, [Reg8, Reg8, Reg8], globals())

DivN = Instruction('DivN', 27, [Reg8, Reg8, Reg8], globals())

Mod = Instruction('Mod', 28, [Reg8, Reg8, Reg8], globals())

Sub = Instruction('Sub', 29, [Reg8, Reg8, Reg8], globals())

SubN = Instruction('SubN', 30, [Reg8, Reg8, Reg8], globals())

LShift = Instruction('LShift', 31, [Reg8, Reg8, Reg8], globals())

RShift = Instruction('RShift', 32, [Reg8, Reg8, Reg8], globals())

URshift = Instruction('URshift', 33, [Reg8, Reg8, Reg8], globals())

BitAnd = Instruction('BitAnd', 34, [Reg8, Reg8, Reg8], globals())

BitXor = Instruction('BitXor', 35, [Reg8, Reg8, Reg8], globals())

BitOr = Instruction('BitOr', 36, [Reg8, Reg8, Reg8], globals())

InstanceOf = Instruction('InstanceOf', 37, [Reg8, Reg8, Reg8], globals())

IsIn = Instruction('IsIn', 38, [Reg8, Reg8, Reg8], globals())

GetEnvironment = Instruction('GetEnvironment', 39, [Reg8, UInt8], globals())

StoreToEnvironment = Instruction('StoreToEnvironment', 40, [Reg8, UInt8, Reg8], globals())

StoreToEnvironmentL = Instruction('StoreToEnvironmentL', 41, [Reg8, UInt16, Reg8], globals())

StoreNPToEnvironment = Instruction('StoreNPToEnvironment', 42, [Reg8, UInt8, Reg8], globals())

StoreNPToEnvironmentL = Instruction('StoreNPToEnvironmentL', 43, [Reg8, UInt16, Reg8], globals())

LoadFromEnvironment = Instruction('LoadFromEnvironment', 44, [Reg8, Reg8, UInt8], globals())

LoadFromEnvironmentL = Instruction('LoadFromEnvironmentL', 45, [Reg8, Reg8, UInt16], globals())

GetGlobalObject = Instruction('GetGlobalObject', 46, [Reg8], globals())

GetNewTarget = Instruction('GetNewTarget', 47, [Reg8], globals())

CreateEnvironment = Instruction('CreateEnvironment', 48, [Reg8], globals())

DeclareGlobalVar = Instruction('DeclareGlobalVar', 49, [UInt32], globals())

DeclareGlobalVar.operands[0].operand_meaning = OperandMeaning.string_id

GetByIdShort = Instruction('GetByIdShort', 50, [Reg8, Reg8, UInt8, UInt8], globals())

GetById = Instruction('GetById', 51, [Reg8, Reg8, UInt8, UInt16], globals())

GetByIdLong = Instruction('GetByIdLong', 52, [Reg8, Reg8, UInt8, UInt32], globals())

GetByIdShort.operands[3].operand_meaning = OperandMeaning.string_id

GetById.operands[3].operand_meaning = OperandMeaning.string_id

GetByIdLong.operands[3].operand_meaning = OperandMeaning.string_id

TryGetById = Instruction('TryGetById', 53, [Reg8, Reg8, UInt8, UInt16], globals())

TryGetByIdLong = Instruction('TryGetByIdLong', 54, [Reg8, Reg8, UInt8, UInt32], globals())

TryGetById.operands[3].operand_meaning = OperandMeaning.string_id

TryGetByIdLong.operands[3].operand_meaning = OperandMeaning.string_id

PutById = Instruction('PutById', 55, [Reg8, Reg8, UInt8, UInt16], globals())

PutByIdLong = Instruction('PutByIdLong', 56, [Reg8, Reg8, UInt8, UInt32], globals())

PutById.operands[3].operand_meaning = OperandMeaning.string_id

PutByIdLong.operands[3].operand_meaning = OperandMeaning.string_id

TryPutById = Instruction('TryPutById', 57, [Reg8, Reg8, UInt8, UInt16], globals())

TryPutByIdLong = Instruction('TryPutByIdLong', 58, [Reg8, Reg8, UInt8, UInt32], globals())

TryPutById.operands[3].operand_meaning = OperandMeaning.string_id

TryPutByIdLong.operands[3].operand_meaning = OperandMeaning.string_id

PutNewOwnByIdShort = Instruction('PutNewOwnByIdShort', 59, [Reg8, Reg8, UInt8], globals())

PutNewOwnById = Instruction('PutNewOwnById', 60, [Reg8, Reg8, UInt16], globals())

PutNewOwnByIdLong = Instruction('PutNewOwnByIdLong', 61, [Reg8, Reg8, UInt32], globals())

PutNewOwnByIdShort.operands[2].operand_meaning = OperandMeaning.string_id

PutNewOwnById.operands[2].operand_meaning = OperandMeaning.string_id

PutNewOwnByIdLong.operands[2].operand_meaning = OperandMeaning.string_id

PutNewOwnNEById = Instruction('PutNewOwnNEById', 62, [Reg8, Reg8, UInt16], globals())

PutNewOwnNEByIdLong = Instruction('PutNewOwnNEByIdLong', 63, [Reg8, Reg8, UInt32], globals())

PutNewOwnNEById.operands[2].operand_meaning = OperandMeaning.string_id

PutNewOwnNEByIdLong.operands[2].operand_meaning = OperandMeaning.string_id

PutOwnByIndex = Instruction('PutOwnByIndex', 64, [Reg8, Reg8, UInt8], globals())

PutOwnByIndexL = Instruction('PutOwnByIndexL', 65, [Reg8, Reg8, UInt32], globals())

PutOwnByVal = Instruction('PutOwnByVal', 66, [Reg8, Reg8, Reg8, UInt8], globals())

DelById = Instruction('DelById', 67, [Reg8, Reg8, UInt16], globals())

DelByIdLong = Instruction('DelByIdLong', 68, [Reg8, Reg8, UInt32], globals())

DelById.operands[2].operand_meaning = OperandMeaning.string_id

DelByIdLong.operands[2].operand_meaning = OperandMeaning.string_id

GetByVal = Instruction('GetByVal', 69, [Reg8, Reg8, Reg8], globals())

PutByVal = Instruction('PutByVal', 70, [Reg8, Reg8, Reg8], globals())

DelByVal = Instruction('DelByVal', 71, [Reg8, Reg8, Reg8], globals())

PutOwnGetterSetterByVal = Instruction('PutOwnGetterSetterByVal', 72, [Reg8, Reg8, Reg8, Reg8, UInt8], globals())

GetPNameList = Instruction('GetPNameList', 73, [Reg8, Reg8, Reg8, Reg8], globals())

GetNextPName = Instruction('GetNextPName', 74, [Reg8, Reg8, Reg8, Reg8, Reg8], globals())

Call = Instruction('Call', 75, [Reg8, Reg8, UInt8], globals())
Call.has_ret_target = True

Construct = Instruction('Construct', 76, [Reg8, Reg8, UInt8], globals())
Construct.has_ret_target = True

Call1 = Instruction('Call1', 77, [Reg8, Reg8, Reg8], globals())
Call1.has_ret_target = True

CallDirect = Instruction('CallDirect', 78, [Reg8, UInt8, UInt16], globals())
CallDirect.has_ret_target = True

Call2 = Instruction('Call2', 79, [Reg8, Reg8, Reg8, Reg8], globals())
Call2.has_ret_target = True

Call3 = Instruction('Call3', 80, [Reg8, Reg8, Reg8, Reg8, Reg8], globals())
Call3.has_ret_target = True

Call4 = Instruction('Call4', 81, [Reg8, Reg8, Reg8, Reg8, Reg8, Reg8], globals())
Call4.has_ret_target = True

CallLong = Instruction('CallLong', 82, [Reg8, Reg8, UInt32], globals())
CallLong.has_ret_target = True

ConstructLong = Instruction('ConstructLong', 83, [Reg8, Reg8, UInt32], globals())
ConstructLong.has_ret_target = True

CallDirectLongIndex = Instruction('CallDirectLongIndex', 84, [Reg8, UInt8, UInt32], globals())
CallDirectLongIndex.has_ret_target = True

CallBuiltin = Instruction('CallBuiltin', 85, [Reg8, UInt8, UInt8], globals())

CallBuiltinLong = Instruction('CallBuiltinLong', 86, [Reg8, UInt8, UInt32], globals())

GetBuiltinClosure = Instruction('GetBuiltinClosure', 87, [Reg8, UInt8], globals())

Ret = Instruction('Ret', 88, [Reg8], globals())

Catch = Instruction('Catch', 89, [Reg8], globals())

DirectEval = Instruction('DirectEval', 90, [Reg8, Reg8], globals())

Throw = Instruction('Throw', 91, [Reg8], globals())

ThrowIfEmpty = Instruction('ThrowIfEmpty', 92, [Reg8, Reg8], globals())

Debugger = Instruction('Debugger', 93, [], globals())

AsyncBreakCheck = Instruction('AsyncBreakCheck', 94, [], globals())

ProfilePoint = Instruction('ProfilePoint', 95, [UInt16], globals())

CreateClosure = Instruction('CreateClosure', 96, [Reg8, Reg8, UInt16], globals())

CreateClosureLongIndex = Instruction('CreateClosureLongIndex', 97, [Reg8, Reg8, UInt32], globals())

CreateGeneratorClosure = Instruction('CreateGeneratorClosure', 98, [Reg8, Reg8, UInt16], globals())

CreateGeneratorClosureLongIndex = Instruction('CreateGeneratorClosureLongIndex', 99, [Reg8, Reg8, UInt32], globals())

CreateAsyncClosure = Instruction('CreateAsyncClosure', 100, [Reg8, Reg8, UInt16], globals())

CreateAsyncClosureLongIndex = Instruction('CreateAsyncClosureLongIndex', 101, [Reg8, Reg8, UInt32], globals())

CreateThis = Instruction('CreateThis', 102, [Reg8, Reg8, Reg8], globals())

SelectObject = Instruction('SelectObject', 103, [Reg8, Reg8, Reg8], globals())

LoadParam = Instruction('LoadParam', 104, [Reg8, UInt8], globals())

LoadParamLong = Instruction('LoadParamLong', 105, [Reg8, UInt32], globals())

LoadConstUInt8 = Instruction('LoadConstUInt8', 106, [Reg8, UInt8], globals())

LoadConstInt = Instruction('LoadConstInt', 107, [Reg8, Imm32], globals())

LoadConstDouble = Instruction('LoadConstDouble', 108, [Reg8, Double], globals())

LoadConstString = Instruction('LoadConstString', 109, [Reg8, UInt16], globals())

LoadConstStringLongIndex = Instruction('LoadConstStringLongIndex', 110, [Reg8, UInt32], globals())

LoadConstString.operands[1].operand_meaning = OperandMeaning.string_id

LoadConstStringLongIndex.operands[1].operand_meaning = OperandMeaning.string_id

LoadConstEmpty = Instruction('LoadConstEmpty', 111, [Reg8], globals())

LoadConstUndefined = Instruction('LoadConstUndefined', 112, [Reg8], globals())

LoadConstNull = Instruction('LoadConstNull', 113, [Reg8], globals())

LoadConstTrue = Instruction('LoadConstTrue', 114, [Reg8], globals())

LoadConstFalse = Instruction('LoadConstFalse', 115, [Reg8], globals())

LoadConstZero = Instruction('LoadConstZero', 116, [Reg8], globals())

CoerceThisNS = Instruction('CoerceThisNS', 117, [Reg8, Reg8], globals())

LoadThisNS = Instruction('LoadThisNS', 118, [Reg8], globals())

ToNumber = Instruction('ToNumber', 119, [Reg8, Reg8], globals())

ToInt32 = Instruction('ToInt32', 120, [Reg8, Reg8], globals())

AddEmptyString = Instruction('AddEmptyString', 121, [Reg8, Reg8], globals())

GetArgumentsPropByVal = Instruction('GetArgumentsPropByVal', 122, [Reg8, Reg8, Reg8], globals())

GetArgumentsLength = Instruction('GetArgumentsLength', 123, [Reg8, Reg8], globals())

ReifyArguments = Instruction('ReifyArguments', 124, [Reg8], globals())

CreateRegExp = Instruction('CreateRegExp', 125, [Reg8, UInt32, UInt32, UInt32], globals())

CreateRegExp.operands[1].operand_meaning = OperandMeaning.string_id

CreateRegExp.operands[2].operand_meaning = OperandMeaning.string_id

SwitchImm = Instruction('SwitchImm', 126, [Reg8, UInt32, Addr32, UInt32, UInt32], globals())

StartGenerator = Instruction('StartGenerator', 127, [], globals())

ResumeGenerator = Instruction('ResumeGenerator', 128, [Reg8, Reg8], globals())

CompleteGenerator = Instruction('CompleteGenerator', 129, [], globals())

CreateGenerator = Instruction('CreateGenerator', 130, [Reg8, Reg8, UInt16], globals())

CreateGeneratorLongIndex = Instruction('CreateGeneratorLongIndex', 131, [Reg8, Reg8, UInt32], globals())

IteratorBegin = Instruction('IteratorBegin', 132, [Reg8, Reg8], globals())

IteratorNext = Instruction('IteratorNext', 133, [Reg8, Reg8, Reg8], globals())

IteratorClose = Instruction('IteratorClose', 134, [Reg8, UInt8], globals())

Jmp = Instruction('Jmp', 135, [Addr8], globals())
JmpLong = Instruction('JmpLong', 136, [Addr32], globals())

JmpTrue = Instruction('JmpTrue', 137, [Addr8, Reg8], globals())
JmpTrueLong = Instruction('JmpTrueLong', 138, [Addr32, Reg8], globals())

JmpFalse = Instruction('JmpFalse', 139, [Addr8, Reg8], globals())
JmpFalseLong = Instruction('JmpFalseLong', 140, [Addr32, Reg8], globals())

JmpUndefined = Instruction('JmpUndefined', 141, [Addr8, Reg8], globals())
JmpUndefinedLong = Instruction('JmpUndefinedLong', 142, [Addr32, Reg8], globals())

SaveGenerator = Instruction('SaveGenerator', 143, [Addr8], globals())
SaveGeneratorLong = Instruction('SaveGeneratorLong', 144, [Addr32], globals())

JLess = Instruction('JLess', 145, [Addr8, Reg8, Reg8], globals())
JLessLong = Instruction('JLessLong', 146, [Addr32, Reg8, Reg8], globals())

JNotLess = Instruction('JNotLess', 147, [Addr8, Reg8, Reg8], globals())
JNotLessLong = Instruction('JNotLessLong', 148, [Addr32, Reg8, Reg8], globals())

JLessN = Instruction('JLessN', 149, [Addr8, Reg8, Reg8], globals())
JLessNLong = Instruction('JLessNLong', 150, [Addr32, Reg8, Reg8], globals())

JNotLessN = Instruction('JNotLessN', 151, [Addr8, Reg8, Reg8], globals())
JNotLessNLong = Instruction('JNotLessNLong', 152, [Addr32, Reg8, Reg8], globals())

JLessEqual = Instruction('JLessEqual', 153, [Addr8, Reg8, Reg8], globals())
JLessEqualLong = Instruction('JLessEqualLong', 154, [Addr32, Reg8, Reg8], globals())

JNotLessEqual = Instruction('JNotLessEqual', 155, [Addr8, Reg8, Reg8], globals())
JNotLessEqualLong = Instruction('JNotLessEqualLong', 156, [Addr32, Reg8, Reg8], globals())

JLessEqualN = Instruction('JLessEqualN', 157, [Addr8, Reg8, Reg8], globals())
JLessEqualNLong = Instruction('JLessEqualNLong', 158, [Addr32, Reg8, Reg8], globals())

JNotLessEqualN = Instruction('JNotLessEqualN', 159, [Addr8, Reg8, Reg8], globals())
JNotLessEqualNLong = Instruction('JNotLessEqualNLong', 160, [Addr32, Reg8, Reg8], globals())

JGreater = Instruction('JGreater', 161, [Addr8, Reg8, Reg8], globals())
JGreaterLong = Instruction('JGreaterLong', 162, [Addr32, Reg8, Reg8], globals())

JNotGreater = Instruction('JNotGreater', 163, [Addr8, Reg8, Reg8], globals())
JNotGreaterLong = Instruction('JNotGreaterLong', 164, [Addr32, Reg8, Reg8], globals())

JGreaterN = Instruction('JGreaterN', 165, [Addr8, Reg8, Reg8], globals())
JGreaterNLong = Instruction('JGreaterNLong', 166, [Addr32, Reg8, Reg8], globals())

JNotGreaterN = Instruction('JNotGreaterN', 167, [Addr8, Reg8, Reg8], globals())
JNotGreaterNLong = Instruction('JNotGreaterNLong', 168, [Addr32, Reg8, Reg8], globals())

JGreaterEqual = Instruction('JGreaterEqual', 169, [Addr8, Reg8, Reg8], globals())
JGreaterEqualLong = Instruction('JGreaterEqualLong', 170, [Addr32, Reg8, Reg8], globals())

JNotGreaterEqual = Instruction('JNotGreaterEqual', 171, [Addr8, Reg8, Reg8], globals())
JNotGreaterEqualLong = Instruction('JNotGreaterEqualLong', 172, [Addr32, Reg8, Reg8], globals())

JGreaterEqualN = Instruction('JGreaterEqualN', 173, [Addr8, Reg8, Reg8], globals())
JGreaterEqualNLong = Instruction('JGreaterEqualNLong', 174, [Addr32, Reg8, Reg8], globals())

JNotGreaterEqualN = Instruction('JNotGreaterEqualN', 175, [Addr8, Reg8, Reg8], globals())
JNotGreaterEqualNLong = Instruction('JNotGreaterEqualNLong', 176, [Addr32, Reg8, Reg8], globals())

JEqual = Instruction('JEqual', 177, [Addr8, Reg8, Reg8], globals())
JEqualLong = Instruction('JEqualLong', 178, [Addr32, Reg8, Reg8], globals())

JNotEqual = Instruction('JNotEqual', 179, [Addr8, Reg8, Reg8], globals())
JNotEqualLong = Instruction('JNotEqualLong', 180, [Addr32, Reg8, Reg8], globals())

JStrictEqual = Instruction('JStrictEqual', 181, [Addr8, Reg8, Reg8], globals())
JStrictEqualLong = Instruction('JStrictEqualLong', 182, [Addr32, Reg8, Reg8], globals())

JStrictNotEqual = Instruction('JStrictNotEqual', 183, [Addr8, Reg8, Reg8], globals())
JStrictNotEqualLong = Instruction('JStrictNotEqualLong', 184, [Addr32, Reg8, Reg8], globals())

Add32 = Instruction('Add32', 185, [Reg8, Reg8, Reg8], globals())

Sub32 = Instruction('Sub32', 186, [Reg8, Reg8, Reg8], globals())

Mul32 = Instruction('Mul32', 187, [Reg8, Reg8, Reg8], globals())

Divi32 = Instruction('Divi32', 188, [Reg8, Reg8, Reg8], globals())

Divu32 = Instruction('Divu32', 189, [Reg8, Reg8, Reg8], globals())

Loadi8 = Instruction('Loadi8', 190, [Reg8, Reg8, Reg8], globals())

Loadu8 = Instruction('Loadu8', 191, [Reg8, Reg8, Reg8], globals())

Loadi16 = Instruction('Loadi16', 192, [Reg8, Reg8, Reg8], globals())

Loadu16 = Instruction('Loadu16', 193, [Reg8, Reg8, Reg8], globals())

Loadi32 = Instruction('Loadi32', 194, [Reg8, Reg8, Reg8], globals())

Loadu32 = Instruction('Loadu32', 195, [Reg8, Reg8, Reg8], globals())

Store8 = Instruction('Store8', 196, [Reg8, Reg8, Reg8], globals())

Store16 = Instruction('Store16', 197, [Reg8, Reg8, Reg8], globals())

Store32 = Instruction('Store32', 198, [Reg8, Reg8, Reg8], globals())

CallDirect.operands[2].operand_meaning = OperandMeaning.function_id

CreateClosure.operands[2].operand_meaning = OperandMeaning.function_id

CreateClosureLongIndex.operands[2].operand_meaning = OperandMeaning.function_id

CreateGeneratorClosure.operands[2].operand_meaning = OperandMeaning.function_id

CreateGeneratorClosureLongIndex.operands[2].operand_meaning = OperandMeaning.function_id

CreateGenerator.operands[2].operand_meaning = OperandMeaning.function_id

CreateGeneratorLongIndex.operands[2].operand_meaning = OperandMeaning.function_id

CreateAsyncClosure.operands[2].operand_meaning = OperandMeaning.function_id

CreateAsyncClosureLongIndex.operands[2].operand_meaning = OperandMeaning.function_id

_opcode_to_instruction : Dict[int, Instruction] = {v.opcode: v for v in _instructions}
_name_to_instruction : Dict[str, Instruction] = {v.name: v for v in _instructions}

_builtin_function_names : List[str] = [
    'Array.isArray',
    'ArrayBuffer.isView',
    'Date.UTC',
    'Date.now',
    'Date.parse',
    'JSON.parse',
    'JSON.stringify',
    'Math.abs',
    'Math.acos',
    'Math.asin',
    'Math.atan',
    'Math.atan2',
    'Math.ceil',
    'Math.cos',
    'Math.exp',
    'Math.floor',
    'Math.hypot',
    'Math.imul',
    'Math.log',
    'Math.max',
    'Math.min',
    'Math.pow',
    'Math.random',
    'Math.round',
    'Math.sin',
    'Math.sqrt',
    'Math.tan',
    'Math.trunc',
    'Object.create',
    'Object.defineProperties',
    'Object.defineProperty',
    'Object.freeze',
    'Object.getOwnPropertyDescriptor',
    'Object.getOwnPropertyNames',
    'Object.getPrototypeOf',
    'Object.isExtensible',
    'Object.isFrozen',
    'Object.keys',
    'Object.seal',
    'String.fromCharCode',
    'silentSetPrototypeOf',
    'requireFast',
    'getTemplateObject',
    'ensureObject',
    'getMethod',
    'throwTypeError',
    'generatorSetDelegated',
    'copyDataProperties',
    'copyRestArgs',
    'arraySpread',
    'apply',
    'exportAll',
    'exponentiationOperator',
    'spawnAsync'
]

