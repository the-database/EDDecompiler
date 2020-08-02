from Assembler.InstructionTable import *
from Base.ED63RDEvoBase import *
from GameData.ItemNameMap import *

def GetOpCode(fs):
    return fs.ReadByte()

def WriteOpCode(fs, op):
    return fs.WriteByte(op)

ed63rd_op_table = InstructionTable(GetOpCode, WriteOpCode, DefaultGetLabelName, CODE_PAGE)

InstructionNames = {}

InstructionNames[0x00]  = 'ExitThread'
InstructionNames[0x01]  = 'Return'
InstructionNames[0x02]  = 'Jc'
InstructionNames[0x03]  = 'Jump'
InstructionNames[0x04]  = 'Switch'
InstructionNames[0x05]  = 'Call'
InstructionNames[0x06]  = 'NewScene'
InstructionNames[0x07]  = 'IdleLoop'
InstructionNames[0x08]  = 'Sleep'
InstructionNames[0x09]  = 'SetMapFlags'
InstructionNames[0x0A]  = 'ClearMapFlags'
InstructionNames[0x0B]  = 'FadeToDark'
InstructionNames[0x0C]  = 'FadeToBright'
InstructionNames[0x0D]  = 'OP_0D'
InstructionNames[0x0E]  = 'Fade'
InstructionNames[0x0F]  = 'Battle'
InstructionNames[0x10]  = 'OP_10'
InstructionNames[0x11]  = 'OP_11'
InstructionNames[0x12]  = 'StopSound'
InstructionNames[0x13]  = 'SetPlaceName'
InstructionNames[0x14]  = 'BlurSwitch'
InstructionNames[0x15]  = 'OP_15'
InstructionNames[0x16]  = 'OP_16'
InstructionNames[0x17]  = 'ShowSaveMenu'
InstructionNames[0x18]  = 'OP_18'
InstructionNames[0x19]  = 'EventBegin'
InstructionNames[0x1A]  = 'EventEnd'
InstructionNames[0x1B]  = 'OP_1B'
InstructionNames[0x1C]  = 'OP_1C'
InstructionNames[0x1D]  = 'OP_1D'
InstructionNames[0x1E]  = 'OP_1E'
InstructionNames[0x1F]  = 'OP_1F'
InstructionNames[0x20]  = 'OP_20'
InstructionNames[0x21]  = 'OP_21'
InstructionNames[0x22]  = 'OP_22'
InstructionNames[0x23]  = 'OP_23'
InstructionNames[0x24]  = 'OP_24'
InstructionNames[0x25]  = 'SoundDistance'
InstructionNames[0x26]  = 'SoundLoad'
InstructionNames[0x27]  = 'Yield'
InstructionNames[0x28]  = 'OP_28'
InstructionNames[0x29]  = 'OP_29'
InstructionNames[0x2A]  = 'OP_2A'
InstructionNames[0x2B]  = 'OP_2B'
InstructionNames[0x2C]  = 'OP_2C'
InstructionNames[0x2D]  = 'AddParty'
InstructionNames[0x2E]  = 'RemoveParty'
InstructionNames[0x2F]  = 'ClearParty'
InstructionNames[0x30]  = 'OP_30'
InstructionNames[0x31]  = 'OP_31'
InstructionNames[0x32]  = 'OP_32'
InstructionNames[0x33]  = 'OP_33'
InstructionNames[0x34]  = 'OP_34'
InstructionNames[0x35]  = 'OP_35'
InstructionNames[0x36]  = 'OP_36'
InstructionNames[0x37]  = 'OP_37'
InstructionNames[0x38]  = 'AddSepith'
InstructionNames[0x39]  = 'SubSepith'
InstructionNames[0x3A]  = 'AddMira'
InstructionNames[0x3B]  = 'SubMira'
InstructionNames[0x3C]  = 'OP_3C'
InstructionNames[0x3D]  = 'OP_3D'
InstructionNames[0x3E]  = 'OP_3E'
InstructionNames[0x3F]  = 'OP_3F'
InstructionNames[0x40]  = 'OP_40'
InstructionNames[0x41]  = 'OP_41'
InstructionNames[0x42]  = 'OP_42'
InstructionNames[0x43]  = 'OP_43'
InstructionNames[0x44]  = 'OP_44'
InstructionNames[0x45]  = 'QueueWorkItem'
InstructionNames[0x46]  = 'QueueWorkItem2'
InstructionNames[0x47]  = 'WaitChrThread'
InstructionNames[0x48]  = 'OP_48'
InstructionNames[0x49]  = 'Event'
InstructionNames[0x4A]  = 'OP_4A'
InstructionNames[0x4B]  = 'OP_4B'
InstructionNames[0x4C]  = 'OP_4C'
InstructionNames[0x4D]  = 'RunExpression'
InstructionNames[0x4E]  = 'OP_4E'
InstructionNames[0x4F]  = 'OP_4F'
InstructionNames[0x50]  = 'OP_50'
InstructionNames[0x51]  = 'OP_51'
InstructionNames[0x52]  = 'TalkBegin'
InstructionNames[0x53]  = 'TalkEnd'
InstructionNames[0x54]  = 'AnonymousTalk'
InstructionNames[0x55]  = 'OP_55'
InstructionNames[0x56]  = 'OP_56'
InstructionNames[0x57]  = 'OP_57'
InstructionNames[0x58]  = 'CloseMessageWindow'
InstructionNames[0x59]  = 'OP_59'
InstructionNames[0x5A]  = 'SetMessageWindowPos'
InstructionNames[0x5B]  = 'ChrTalk'
InstructionNames[0x5C]  = 'NpcTalk'
InstructionNames[0x5D]  = 'Menu'
InstructionNames[0x5E]  = 'MenuEnd'
InstructionNames[0x5F]  = 'OP_5F'
InstructionNames[0x60]  = 'SetChrName'
InstructionNames[0x61]  = 'OP_61'
InstructionNames[0x62]  = 'OP_62'
InstructionNames[0x63]  = 'OP_63'
InstructionNames[0x64]  = 'OP_64'
InstructionNames[0x65]  = 'OP_65'
InstructionNames[0x66]  = 'OP_66'
InstructionNames[0x67]  = 'OP_67'
InstructionNames[0x68]  = 'OP_68'
InstructionNames[0x69]  = 'OP_69'
InstructionNames[0x6A]  = 'OP_6A'
InstructionNames[0x6B]  = 'OP_6B'
InstructionNames[0x6C]  = 'OP_6C'
InstructionNames[0x6D]  = 'OP_6D'
InstructionNames[0x6E]  = 'OP_6E'
InstructionNames[0x6F]  = 'OP_6F'
InstructionNames[0x70]  = 'OP_70'
InstructionNames[0x71]  = 'OP_71'
InstructionNames[0x72]  = 'OP_72'
InstructionNames[0x73]  = 'OP_73'
InstructionNames[0x74]  = 'OP_74'
InstructionNames[0x75]  = 'OP_75'
InstructionNames[0x76]  = 'OP_76'
InstructionNames[0x77]  = 'OP_77'
InstructionNames[0x78]  = 'OP_78'
InstructionNames[0x79]  = 'OP_79'
InstructionNames[0x7A]  = 'OP_7A'
InstructionNames[0x7B]  = 'OP_7B'
InstructionNames[0x7C]  = 'OP_7C'
InstructionNames[0x7D]  = 'OP_7D'
InstructionNames[0x7E]  = 'OP_7E'
InstructionNames[0x7F]  = 'LoadEffect'
InstructionNames[0x80]  = 'PlayEffect'
InstructionNames[0x81]  = 'Play3DEffect'
InstructionNames[0x82]  = 'OP_82'
InstructionNames[0x83]  = 'OP_83'
InstructionNames[0x84]  = 'OP_84'
InstructionNames[0x85]  = 'OP_85'
InstructionNames[0x86]  = 'SetChrChipByIndex'
InstructionNames[0x87]  = 'SetChrSubChip'
InstructionNames[0x88]  = 'SetChrPos'
InstructionNames[0x89]  = 'OP_89'
InstructionNames[0x8A]  = 'TurnDirection'
InstructionNames[0x8B]  = 'OP_8B'
InstructionNames[0x8C]  = 'OP_8C'
InstructionNames[0x8D]  = 'OP_8D'
InstructionNames[0x8E]  = 'OP_8E'
InstructionNames[0x8F]  = 'OP_8F'
InstructionNames[0x90]  = 'OP_90'
InstructionNames[0x91]  = 'OP_91'
InstructionNames[0x92]  = 'OP_92'
InstructionNames[0x93]  = 'OP_93'
InstructionNames[0x94]  = 'OP_94'
InstructionNames[0x95]  = 'OP_95'
InstructionNames[0x96]  = 'OP_96'
InstructionNames[0x97]  = 'OP_97'
InstructionNames[0x98]  = 'OP_98'
InstructionNames[0x99]  = 'OP_99'
InstructionNames[0x9A]  = 'SetChrFlags'
InstructionNames[0x9B]  = 'ClearChrFlags'
InstructionNames[0x9C]  = 'SetChrBattleFlags'
InstructionNames[0x9D]  = 'ClearChrBattleFlags'
InstructionNames[0x9E]  = 'OP_9E'
InstructionNames[0x9F]  = 'OP_9F'
InstructionNames[0xA0]  = 'OP_A0'
InstructionNames[0xA1]  = 'OP_A1'
InstructionNames[0xA2]  = 'OP_A2'
InstructionNames[0xA3]  = 'OP_A3'
InstructionNames[0xA4]  = 'OP_A4'
InstructionNames[0xA5]  = 'OP_A5'
InstructionNames[0xA6]  = 'OP_A6'
InstructionNames[0xA7]  = 'OP_A7'
InstructionNames[0xA8]  = 'OP_A8'
InstructionNames[0xA9]  = 'OP_A9'
InstructionNames[0xAA]  = 'OP_AA'
InstructionNames[0xAB]  = 'OP_AB'
InstructionNames[0xAC]  = 'OP_AC'
InstructionNames[0xAD]  = 'OP_AD'
InstructionNames[0xAE]  = 'OP_AE'
InstructionNames[0xAF]  = 'OP_AF'
InstructionNames[0xB0]  = 'OP_B0'
InstructionNames[0xB1]  = 'OP_B1'
InstructionNames[0xB2]  = 'OP_B2'
InstructionNames[0xB3]  = 'PlayMovie'
InstructionNames[0xB4]  = 'OP_B4'
InstructionNames[0xB5]  = 'OP_B5'
InstructionNames[0xB6]  = 'OP_B6'
InstructionNames[0xB7]  = 'OP_B7'
InstructionNames[0xB8]  = 'OP_B8'
InstructionNames[0xB9]  = 'OP_B9'
InstructionNames[0xBA]  = 'OP_BA'
InstructionNames[0xBB]  = 'OP_BB'
InstructionNames[0xBC]  = 'OP_BC'
InstructionNames[0xBD]  = 'OP_BD'
InstructionNames[0xBE]  = 'OP_BE'
InstructionNames[0xBF]  = 'OP_BF'
InstructionNames[0xC0]  = 'OP_C0'
InstructionNames[0xC1]  = 'OP_C1'
InstructionNames[0xC2]  = 'OP_C2'
InstructionNames[0xC3]  = 'OP_C3'
InstructionNames[0xC4]  = 'OP_C4'
InstructionNames[0xC5]  = 'OP_C5'
InstructionNames[0xC6]  = 'OP_C6'
InstructionNames[0xC7]  = 'OP_C7'
InstructionNames[0xC8]  = 'OP_C8'
InstructionNames[0xC9]  = 'OP_C9'
InstructionNames[0xCA]  = 'OP_CA'
InstructionNames[0xCB]  = 'OP_CB'
InstructionNames[0xCC]  = 'OP_CC'
InstructionNames[0xCD]  = 'OP_CD'
InstructionNames[0xCE]  = 'OP_CE'
InstructionNames[0xCF]  = 'OP_CF'
InstructionNames[0xD0]  = 'OP_D0'
InstructionNames[0xD1]  = 'OP_D1'
InstructionNames[0xD2]  = 'OP_D2'
InstructionNames[0xD3]  = 'OP_D3'
InstructionNames[0xD4]  = 'OP_D4'
InstructionNames[0xD5]  = 'OP_D5'
InstructionNames[0xD6]  = 'OP_D6'
InstructionNames[0xD7]  = 'OP_D7'
InstructionNames[0xD8]  = 'OP_D8'
InstructionNames[0xD9]  = 'OP_D9'  # Max in ori PC
InstructionNames[0xDA]  = 'OP_DA'
InstructionNames[0xDB]  = 'OP_DB'
InstructionNames[0xDC]  = 'OP_DC'
InstructionNames[0xDD]  = 'OP_DD'
InstructionNames[0xDE]  = 'OP_DE'
InstructionNames[0xDF]  = 'OP_DF'
InstructionNames[0xE0]  = 'OP_E0'
InstructionNames[0xE1]  = 'OP_E1'
InstructionNames[0xE2]  = 'OP_E2'
InstructionNames[0xE3]  = 'OP_E3'
InstructionNames[0xE4]  = 'OP_E4'
InstructionNames[0xE5]  = 'OP_E5'
InstructionNames[0xE6]  = 'OP_E6'
InstructionNames[0xE7]  = 'OP_E7'
InstructionNames[0xEA]  = 'OP_EA'
InstructionNames[0xF7]  = 'OP_F7'

InstructionNames[0xE8]  = 'OP_E8'
InstructionNames[0xE9]  = 'OP_E9'
InstructionNames[0xED]  = 'OP_ED'
InstructionNames[0xF0]  = 'OP_F0'
InstructionNames[0xF1]  = 'OP_F1'
InstructionNames[0xF2]  = 'OP_F2'
InstructionNames[0xF3]  = 'OP_F3'
InstructionNames[0xF5]  = 'OP_F5'
InstructionNames[0xF8]  = 'OP_F8'
InstructionNames[0xF9]  = 'OP_F9'
InstructionNames[0xFA]  = 'OP_FA'
InstructionNames[0xFB]  = 'OP_FB'
InstructionNames[0xFC]  = 'OP_FC'
InstructionNames[0xFD]  = 'OP_FD'
InstructionNames[0xFE]  = 'OP_FE'


for op, name in InstructionNames.items():
    expr = '%s = 0x%08X' % (name, op)
    exec(expr)


def GetItemName(id):
    return '0x%X' % id
    #return ItemNameMap[id] if id in ItemNameMap else '0x%X' % id

def GetItemDisplayName(id):
    return '0x%X' % id
    #return '\'%s\'' % ItemTrueNameMap[id] if id in ItemTrueNameMap else '0x%X' % id


ScpStrCodeMap = {}

ScpStrCodeMap[-1]       = 'SCPSTR_CODE_STRING'
ScpStrCodeMap[0x1F]     = 'SCPSTR_CODE_ITEM'
ScpStrCodeMap[0x01]     = 'SCPSTR_CODE_LINE_FEED'
ScpStrCodeMap[0x02]     = 'SCPSTR_CODE_ENTER'
ScpStrCodeMap[0x03]     = 'SCPSTR_CODE_CLEAR'
ScpStrCodeMap[0x05]     = 'SCPSTR_CODE_05'
ScpStrCodeMap[0x07]     = 'SCPSTR_CODE_COLOR'
ScpStrCodeMap[0x09]     = 'SCPSTR_CODE_09'

for code, name in ScpStrCodeMap.items():
    expr = '%s = %d' % (name, code)
    exec(expr)

def GetStrCode(code):
    return ScpStrCodeMap[code] if code in ScpStrCodeMap else '0x%X' % code

class ScpString:
    def __init__(self, CtrlCode, Value = None):
        self.CtrlCode   = CtrlCode
        self.Value      = Value

    def binary(self):
        pass

    def dump(self):
        return {
            'CtrlCode': self.CtrlCode,
            'Value': self.Value
        }

    def __str__(self):
        if self.CtrlCode == SCPSTR_CODE_STRING:
            return '"%s"' % self.Value

        value = self.Value
        code = GetStrCode(self.CtrlCode)

        if value == None:
            return 'scpstr(%s)' % code

        value = GetItemDisplayName(value) if self.CtrlCode == SCPSTR_CODE_ITEM else '0x%X' % value

        return 'scpstr(%s, %s)' % (code, value)

    __repr__ = __str__

def BuildStringListFromObjectList(strlist):
    s = []
    laststrindex = None
    for x in strlist:
        if x.CtrlCode in [SCPSTR_CODE_LINE_FEED, SCPSTR_CODE_ENTER, SCPSTR_CODE_CLEAR, SCPSTR_CODE_05, SCPSTR_CODE_COLOR, SCPSTR_CODE_09]:
            if len(s) != laststrindex:
                s.append(str(x))

            else:
                if x.CtrlCode == SCPSTR_CODE_COLOR:
                    tmp = '\\x%02X\\x%02X' % (x.CtrlCode, x.Value)
                else:
                    tmp = '\\x%02X' % x.CtrlCode
                s[-1] = '"%s%s"' % (s[-1][1:-1], tmp)

        elif x.CtrlCode == SCPSTR_CODE_STRING:

            s.append(str(x))
            laststrindex = len(s)

        else:

            s.append(str(x))

    return s

def FormatFuncString(data, oprfmt, mark_number = None):

    entry = data.TableEntry
    ins = data.Instruction

    txt = [ '', '%s(' % entry.OpName ]

    maxlen = 0

    for i in range(len(oprfmt)):
        opr = oprfmt[i]
        if opr != 'S':
            paramlist = BuildFormatOperandParameterList([opr], [ins.Operand[i]])
            txt.append('    %s,' % entry.FormatAllOperand(paramlist))
            #bp()
            #txt.append('    0x%X,' % ins.Operand[i])
        else:
            strlist = BuildStringListFromObjectList(ins.Operand[i])

            if len(strlist) == 1:
                s = '    %s' % strlist[0]

                if i != len(oprfmt):
                    s += ','

                txt.append(s)
                continue

            index = 0
            txt.append('    (')
            for s in strlist:
                tmp = '        %s,' % s
                if mark_number:
                    if strlen(tmp) > maxlen:
                        maxlen = strlen(tmp)

                    tmp = ljust_cn(tmp, mark_number)
                    tmp += ' # %d' % index

                txt.append(tmp)
                index += 1

            txt.append('    )')

    if mark_number == -1 and maxlen != 0:
        return FormatFuncString(data, oprfmt, maxlen + 5)

    txt.append(')')
    txt.append('')

    return txt

class ED6FCScenaInstructionTableEntry(InstructionTableEntry):
    def __init__(self, op, name = '', operand = NO_OPERAND, flags = 0, handler = None):
        super().__init__(op, name, operand, flags, handler)

    def WriteOperand(self, data, opr, value):

        fs = data.FileStream
        labels = data.Instruction.Labels
        
        def enc_str(str):
            ret = bytearray()
            i = 0
            while i < len(str):
                if ord(str[i]) == SCPSTR_CODE_ITEM:
                    ret.append(ord(str[i]))
                    ret.append(ord(str[i+1]))
                    ret.append(ord(str[i+2]))
                    i += 3
                elif ord(str[i]) == SCPSTR_CODE_COLOR:
                    ret.append(ord(str[i]))
                    ret.append(ord(str[i+1]))
                    i += 2
                elif ord(str[i]) < 0x20:
                    ret.append(ord(str[i]))
                    i += 1
                else:
                    ret.extend(str[i].encode(CODE_PAGE))
                    i += 1
            return bytes(ret)

        def wexpr(value):
            for expr in value:
                expr.WriteExpression(data)

        def wstr(value, recursion = False):
            if type(value) == str:
                value = enc_str(value)
                if not recursion:
                    value += b'\x00'

            elif type(value) == bytes:
                if not recursion:
                    value += b'\x00'

            elif IsTupleOrList(value):
                for x in value:
                    wstr(x, True)

                fs.WriteByte(0)
                return

            fs.write(value)

        oprtype = \
        {
            'E' : wexpr,
            'S' : wstr,
            'M' : lambda value : fs.WriteShort(BGMFileIndex(value).Index()),
            'T' : lambda value : fs.WriteUShort(ItemTrueNameMap[value] if type(value) == str else value),
        }

        if opr == 'O':
            opr = 'o'

        return oprtype[opr](value) if opr in oprtype else super().WriteOperand(data, opr, value)

    def FormatOperand(self, param):
        value   = param.Value
        opr     = param.Operand
        flags   = param.Flags

        def formatstr(strlist):
            s = BuildStringListFromObjectList(strlist)

            if not flags.ArgNewLine:
                if len(s) == 0:
                    return '""'
                elif len(s) == 1:
                    return s[0]

                return '(' + ', '.join(s) + ')'

            raise Exception('not implement')

        def formatbgm(bgm):
            bgm = BGMFileIndex(bgm)
            return ('"%s"' % bgm.Name()) if not bgm.IsInvalid() else ('0x%08X' % (bgm.Index() & 0xFFFFFFFF))

        oprtype = \
        {
            'E' : lambda : FormatExpressionList(value),
            'S' : lambda : formatstr(value),
            'M' : lambda : BGMFileIndex(value).param(),
            'T' : lambda : GetItemDisplayName(value),
        }

        return oprtype[opr]() if opr in oprtype else super().FormatOperand(param)

    def GetOperand(self, opr, fs):

        def readstr():
            string = []
            tmpstr = ''

            while True:
                buf = fs.read(1)

                if buf < b' ':
                    if tmpstr != '':
                        string.append(ScpString(SCPSTR_CODE_STRING, tmpstr.replace('\\', '\\\\')))
                        tmpstr = ''

                    code = struct.unpack('<B', buf)[0]

                    if code == 0:
                        break

                    strobj = ScpString(code)

                    if code == SCPSTR_CODE_COLOR:

                        # dummy byte ?
                        strobj.Value = fs.ReadByte()

                    elif code == SCPSTR_CODE_LINE_FEED or code == 0x0A:

                        # line feed
                        pass

                    elif code == SCPSTR_CODE_ENTER:

                        # need press enter
                        pass

                    elif code == SCPSTR_CODE_CLEAR or code == 0x04:

                        # unknown
                        pass

                    elif code == 0x05:

                        pass

                    elif code == 0x06:

                        # unknown
                        pass

                    elif code == 0x18:

                        pass

                    elif code == SCPSTR_CODE_ITEM:

                        # item id
                        strobj.Value = fs.ReadUShort()

                    string.append(strobj)

                    continue

                elif ('932' in self.Container.CodePage or 'jis' in self.Container.CodePage.lower()) and b'\xA0' <= buf <= b'\xDF':
                    pass

                elif buf >= b'\x80':

                    buf += fs.read(1)

                tmpstr += buf.decode(self.Container.CodePage)

            return string

        oprtype = \
        {
            'S' : readstr,
            'M' : lambda : fs.ReadShort(),
            'T' : lambda : fs.ReadUShort(),
            'O' : lambda : fs.ReadUShort(),
        }

        return oprtype[opr]() if opr in oprtype else super().GetOperand(opr, fs)

    def GetOperandSize(self, opr, fs):
        if opr in ['M', 'O']:
            return 2

        if opr != 'S':
            return super().GetOperandSize(opr, fs)

        pos = fs.tell()
        self.GetOperand(opr, fs)
        oprsize = fs.tell() - pos
        fs.seek(pos)
        return oprsize

def inst(op, operand = NO_OPERAND, flags = 0, handler = None):
    return ED6FCScenaInstructionTableEntry(op, InstructionNames[op], operand, flags, handler)

ExpressionOperantions = {}

ExpressionOperantions[0x00] = 'EXPR_PUSH_LONG'
ExpressionOperantions[0x01] = 'EXPR_END'
ExpressionOperantions[0x02] = 'EXPR_EQU'
ExpressionOperantions[0x03] = 'EXPR_NEQ'
ExpressionOperantions[0x04] = 'EXPR_LSS'
ExpressionOperantions[0x05] = 'EXPR_GTR'
ExpressionOperantions[0x06] = 'EXPR_LEQ'
ExpressionOperantions[0x07] = 'EXPR_GE'
ExpressionOperantions[0x08] = 'EXPR_EQUZ'
ExpressionOperantions[0x09] = 'EXPR_NEQUZ_I64'
ExpressionOperantions[0x0A] = 'EXPR_AND'
ExpressionOperantions[0x0B] = 'EXPR_OR'
ExpressionOperantions[0x0C] = 'EXPR_ADD'
ExpressionOperantions[0x0D] = 'EXPR_SUB'
ExpressionOperantions[0x0E] = 'EXPR_NEG'
ExpressionOperantions[0x0F] = 'EXPR_XOR'
ExpressionOperantions[0x10] = 'EXPR_IMUL'
ExpressionOperantions[0x11] = 'EXPR_IDIV'
ExpressionOperantions[0x12] = 'EXPR_IMOD'
ExpressionOperantions[0x13] = 'EXPR_STUB'
ExpressionOperantions[0x14] = 'EXPR_IMUL_SAVE'
ExpressionOperantions[0x15] = 'EXPR_IDIV_SAVE'
ExpressionOperantions[0x16] = 'EXPR_IMOD_SAVE'
ExpressionOperantions[0x17] = 'EXPR_ADD_SAVE'
ExpressionOperantions[0x18] = 'EXPR_SUB_SAVE'
ExpressionOperantions[0x19] = 'EXPR_AND_SAVE'
ExpressionOperantions[0x1A] = 'EXPR_XOR_SAVE'
ExpressionOperantions[0x1B] = 'EXPR_OR_SAVE'
ExpressionOperantions[0x1C] = 'EXPR_EXEC_OP'
ExpressionOperantions[0x1D] = 'EXPR_NOT'
ExpressionOperantions[0x1E] = 'EXPR_TEST_SCENA_FLAGS'
ExpressionOperantions[0x1F] = 'EXPR_GET_RESULT'
ExpressionOperantions[0x20] = 'EXPR_PUSH_VALUE_INDEX'
ExpressionOperantions[0x21] = 'EXPR_GET_CHR_WORK'
ExpressionOperantions[0x22] = 'EXPR_RAND'
ExpressionOperantions[0x23] = 'EXPR_23'

for opr, expr in ExpressionOperantions.items():
    exec('EXPR_%02X = 0x%X' % (opr, opr))
    exec('%s = 0x%X' % (expr, opr))

class ScpExpression:
    def __init__(self, operation = None, operand = None):
        self.Operation = operation
        self.Operand = operand if operand != None else []

    def binary(self):
        return b''

    def WriteExpression(self, handlerdata):

        operation = self.Operation
        fs = handlerdata.FileStream

        def expr_exec():
            handlerdata.Assemble(self.Operand[0])

        operationmap = \
        {
            EXPR_PUSH_LONG          : lambda : fs.WriteULong(self.Operand[0]),
            EXPR_TEST_SCENA_FLAGS   : lambda : fs.WriteUShort(self.Operand[0]),
            EXPR_GET_RESULT         : lambda : fs.WriteUShort(self.Operand[0]),
            EXPR_PUSH_VALUE_INDEX   : lambda : fs.WriteByte(self.Operand[0]),
            EXPR_23                 : lambda : fs.WriteByte(self.Operand[0]),
            EXPR_GET_CHR_WORK       : lambda : fs.write(struct.pack('<HB', *self.Operand)),
            EXPR_EXEC_OP            : lambda : handlerdata.Assemble(self.Operand[0]),
        }

        fs.WriteByte(operation)

        if operation in operationmap:
            operationmap[operation]()

    def __str__(self):
        if self.Operation == EXPR_TEST_SCENA_FLAGS:

            offset, bit = SplitScenarioFlags(self.Operand[0])
            return 'scpexpr(%s, MakeScenarioFlags(0x%X, %d))' % (ExpressionOperantions[self.Operation], offset, bit)

        elif self.Operation != EXPR_EXEC_OP:

            txt = 'scpexpr(%s' % ExpressionOperantions[self.Operation]
            for opr in self.Operand:
                txt += ', 0x%X' % opr

            txt += ')'
            return txt

        from Assembler import Assembler2

        asm = Assembler2.Disassembler(ed63rd_op_table)

        txt = 'scpexpr(%s' % ExpressionOperantions[self.Operation]
        for inst in self.Operand:
            data = HandlerData(HANDLER_REASON_FORMAT)
            data.Instruction    = inst
            data.TableEntry     = ed63rd_op_table[inst.OpCode]
            txt += ', "%s"' % CombineMultiline(asm.FormatInstruction(data))

        txt += ')'
        return txt

def FormatExpressionList(exprlist):
    exprtxt = '%s' % exprlist[0]
    for expr in exprlist[1:]:
        exprtxt += ', %s' % expr

    return '(%s)' % exprtxt

def ParseScpExpression(data):
    expr = []
    fs = data.FileStream

    # stack size == 0xB0 ?

    while True:
        operation = fs.ReadByte()

        scpexpr = ScpExpression(operation)

        if operation == EXPR_PUSH_LONG:

            scpexpr.Operand.append(fs.ReadULong())

        elif operation == EXPR_END:

            break

        elif operation in [
                    EXPR_EQU,
                    EXPR_NEQ,
                    EXPR_LSS,
                    EXPR_GTR,
                    EXPR_LEQ,
                    EXPR_GE,
                    EXPR_EQUZ,
                    EXPR_NEQUZ_I64,
                    EXPR_AND,
                    EXPR_OR,
                    EXPR_ADD,
                    EXPR_SUB,
                    EXPR_NEG,
                    EXPR_XOR,
                    EXPR_IMUL,
                    EXPR_IDIV,
                    EXPR_IMOD,
                    EXPR_STUB,
                    EXPR_IMUL_SAVE,
                    EXPR_IDIV_SAVE,
                    EXPR_IMOD_SAVE,
                    EXPR_ADD_SAVE,
                    EXPR_SUB_SAVE,
                    EXPR_AND_SAVE,
                    EXPR_XOR_SAVE,
                    EXPR_OR_SAVE,
                    EXPR_NOT,
                ]:
            # pop all operand, and push result
            pass

        elif operation == EXPR_EXEC_OP:

            # execute one op code

            execdata = data.CreateBranch()
            #execdata.Instruction.OpCode = data.TableEntry.Container.GetOpCode(fs)
            #execdata.TableEntry = data.TableEntry.Container[execdata.Instruction.OpCode]
            execinst = execdata.Disasm(execdata)
            scpexpr.Operand.append(execinst)

        elif operation == EXPR_TEST_SCENA_FLAGS or \
             operation == EXPR_GET_RESULT:

            scpexpr.Operand.append(fs.ReadUShort())

        elif operation == EXPR_PUSH_VALUE_INDEX:

            scpexpr.Operand.append(fs.ReadByte())

        elif operation == EXPR_GET_CHR_WORK:

            scpexpr.Operand.append(fs.ReadUShort())
            scpexpr.Operand.append(fs.ReadByte())

        elif operation == EXPR_RAND:

            pass

        elif operation == EXPR_23:

            scpexpr.Operand.append(fs.ReadByte())

        expr.append(scpexpr)

    expr.append(scpexpr)

    return expr

def scp_if(data):
    # if (expression)
    #   goto offset

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        expr = ParseScpExpression(data)
        ins.Operand.append(expr)

        offset = fs.ReadUShort()
        ins.Operand.append(offset)
        ins.BranchTargets.append(offset)

        ins.OperandFormat = 'EO'

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'EO'
        return None

SWITCH_DEFAULT  = -1

def scp_not_implemented(data):
    fs = data.FileStream
    raise NotImplementedError('%X @ %X' % (data.Instruction.OpCode, fs.Position - 1))

def scp_switch(data):

    # switch (expression)
    #     case option_id:
    #         goto option_offset;
    #     default:
    #         goto default_offset

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        expr = ParseScpExpression(data)
        optioncount = fs.ReadUShort()
        options = []

        for i in range(optioncount):
            optionid, optionoffset = struct.unpack('<HH', fs.read(4))
            options.append((optionid, optionoffset))
            ins.BranchTargets.append(optionoffset)

        defaultoffset = fs.ReadUShort()

        ins.BranchTargets.insert(0, defaultoffset)

        ins.Operand.append(expr)
        ins.Operand.append(options)
        ins.Operand.append(defaultoffset)

        return ins

    elif data.Reason == HANDLER_REASON_FORMAT:
        #   switch(
        #       Expression,
        #       (CaseID, CaseLabel),
        #       (CaseID, CaseLabel),
        #       (CaseID, CaseLabel),
        #       (-1,    DefaultLabel)
        #   )

        ins = data.Instruction
        entry = data.TableEntry

        txt = []
        txt.append('%s(' % entry.OpName)
        txt.append('    %s,' % FormatExpressionList(ins.Operand[0]))

        GetLabelName = entry.Container.GetLabelName
        #txt.append('    (')

        for case in ins.Operand[1]:
            txt.append('    (%d, "%s"),' % (case[0], GetLabelName(case[1])))

        txt.append('    (SWITCH_DEFAULT, "%s"),' % GetLabelName(ins.Operand[-1]))
        #txt.append('    )')
        txt.append(')')
        txt.append('')

        return txt

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        fs      = data.FileStream
        args    = data.Arguments
        entry   = data.TableEntry
        inst    = data.Instruction

        exprlist = args[0]
        optlist = args[1:]

        opts = []
        defaultoffset = None
        for opt in optlist:
            if opt[0] == SWITCH_DEFAULT:
                if defaultoffset != None:
                    raise Exception('multi default case')

                defaultoffset = opt[1]
            else:
                opts.append(opt)

        optlist = opts

        entry.Container.WriteOpCode(fs, inst.OpCode)

        for expr in exprlist:
            expr.WriteExpression(data)

        entry.WriteOperand(data, 'W', len(optlist))

        for opt in optlist:
            fs.WriteUShort(opt[0])
            inst.Labels.append(LabelEntry(opt[1], fs.tell()))
            fs.WriteUShort(INVALID_OFFSET)

        inst.Labels.append(LabelEntry(defaultoffset, fs.tell()))
        fs.WriteUShort(INVALID_OFFSET)

        return inst

def scp_new_scene(data):

    if data.Reason == HANDLER_REASON_DISASM:

        data.Instruction.OperandFormat = 'LCCC'

    elif data.Reason == HANDLER_REASON_FORMAT:

        ins = data.Instruction

        symbol = '%s("%s", %d, %d, %d)' % (
                    data.TableEntry.OpName, ScenarioFileIndex(ins.Operand[0]).Name(),
                    ins.Operand[1], ins.Operand[2], ins.Operand[3]
                )

        return [symbol]

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Arguments[0] = ScenarioFileIndex(data.Arguments[0]).Index()
        data.Instruction.OperandFormat = 'LCCC'

def scp_battle(data):

    operand_with_battle_info = 'LLBWB'

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction
        entry = data.TableEntry

        battleIndex, opr2 = entry.GetAllOperand('LL', fs)

        ins.Operand.append(battleIndex)
        ins.Operand.append(opr2)

        ins.Operand.append(fs.ReadByte())
        ins.Operand.append(fs.ReadUShort())
        ins.Operand.append(fs.ReadByte())

        ins.OperandFormat = operand_with_battle_info

        return ins

    elif data.Reason == HANDLER_REASON_FORMAT:

        pass

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        ins = data.Instruction
        BattleInfoOffset = data.Arguments[0]
        ins.OperandFormat = operand_with_battle_info

def scp_16(data):
    def getopr(opr1):
        return 'LLLL' if opr1 == 2 else ''

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction
        entry = data.TableEntry

        opr1 = entry.GetOperand('B', fs)

        operand = getopr(opr1)

        ins.Operand.append(opr1)
        ins.Operand += entry.GetAllOperand(operand, fs)

        ins.OperandFormat = 'B' + operand

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        opr1 = data.Arguments[0]
        operand = getopr(opr1)

        data.Instruction.OperandFormat = 'B' + operand

def scp_28(data):

    def getopr(opr2):
        operand = ''

        if opr2 == 1 or opr2 == 2:
            operand = 'W'
        elif opr2 == 3 or opr2 == 4:
            operand = 'B'

        return operand

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        opr1, opr2 = data.TableEntry.GetAllOperand('WB', fs)

        ins.Operand.append(opr1)
        ins.Operand.append(opr2)

        operand = getopr(opr2)

        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        ins.OperandFormat = 'WB' + operand

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'WB' + getopr(data.Arguments[1])

def scp_29(data):

    def getopr(opr2):
        return 'W' if opr2 == 1 else 'B'

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        opr1, opr2 = data.TableEntry.GetAllOperand('WB', fs)

        ins.Operand.append(opr1)
        ins.Operand.append(opr2)

        operand = getopr(opr2)

        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        ins.OperandFormat = 'WB' + operand

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        opr2 = data.Arguments[1]
        data.Instruction.OperandFormat = 'WB' + getopr(opr2)

def scp_2a(data):

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        for i in range(0xC):
            opr = fs.ReadUShort()
            ins.Operand.append(opr)
            if opr == 0xFFFF:
                break

        ins.OperandFormat = 'W' * len(ins.Operand)

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'W' * min(0xC, len(data.Arguments))

def scp_37(data):
    def getopr(opr2):
        return 'B' if 0x7F <= opr2 <= 0x87 else ''

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        opr = 'BB'
        ins.OperandFormat = opr
        ins.Operand = data.TableEntry.GetAllOperand(opr, fs)

        operand = getopr(ins.Operand[1])
        ins.OperandFormat += operand
        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        opr2 = data.Arguments[1]

        data.Instruction.OperandFormat = 'BB' + getopr(opr2)

LAMBDA_INDEX = 0
def ResetLabmdaIndex():
    global LAMBDA_INDEX
    LAMBDA_INDEX = 0

def scp_lambda_worker(data, extra_length):

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        target, tid, length = data.TableEntry.GetAllOperand('WWB', fs)

        block = None
        if length != 0:
            length += extra_length
            pos = fs.tell()
            block = data.DisasmBlock(pos, length)
            fs.seek(pos + length)

        ins.Operand = [target, tid, block]

        return ins

    elif data.Reason == HANDLER_REASON_FORMAT:

        '''

        def lambda_xxx():
            OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
            OP_00()

        X(ChrId, ChrThreadId, lambda_xxx)

        '''

        ins = data.Instruction
        entry = data.TableEntry
        target, tid, lambdablock = ins.Operand

        if lambdablock is None:
            return ['', '%s(0x%X, %d, %s)' % (data.TableEntry.OpName, target, tid, lambdablock)]

        lambda_name = ''
        global LAMBDA_INDEX
        if USE_INDEX_LABEL_NAME:
            lambda_name = 'lambda_%d' % LAMBDA_INDEX
            LAMBDA_INDEX += 1
        else:
            lambda_name = 'lambda_%X' % lambdablock.Offset

        txt = ['', 'def %s():' % lambda_name]

        for inst in lambdablock.Instructions:
            lambdadata = data.CreateBranch()
            lambdadata.Instruction = inst
            lambdabody = lambdadata.Format(lambdadata)
            for i in range(len(lambdabody)):
                if lambdabody[i] == '':
                    continue
                lambdabody[i] = '    ' + lambdabody[i]

            txt += lambdabody

        txt.append('')

        txt.append('%s(0x%X, %d, %s)' % (data.TableEntry.OpName, target, tid, lambda_name))

        return txt


    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        fs      = data.FileStream
        entry   = data.TableEntry
        inst    = data.Instruction

        target, tid, lambdafunc = data.Arguments

        entry.Container.WriteOpCode(fs, inst.OpCode)

        entry.WriteOperand(data, 'W', target)
        entry.WriteOperand(data, 'W', tid)

        if lambdafunc is None:
            entry.WriteOperand(data, 'B', 0)
        else:
            fs.seek(1, io.SEEK_CUR)
            pos = fs.tell()

            lambdafunc()

            pos2 = fs.tell()

            if pos2 - pos > 0xFF:
                raise Exception('lambda must be smaller than 0x100 bytes: current = %X' % (pos2 - pos))

            fs.seek(pos - 1)
            entry.WriteOperand(data, 'B', pos2 - pos - extra_length)

            fs.seek(pos2)

        return inst

def scp_42(data):

    raise

    def getopr(opr1):
        return 'B' if opr1 in [0x28A, 0x28B, 0x28E, 0x28F, 0x291, 0x2D0, 0x2D1, 0x2D2, 0x2D3, 0x2D4] else ''

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction
        entry = data.TableEntry

        opr1 = entry.GetAllOperand('B', fs)
        operand = getopr(opr1)

        ins.Operand.append(itemid)
        ins.Operand.append(opr2)
        ins.Operand.extend(data.TableEntry.GetAllOperand(operand, fs))

        ins.OperandFormat = 'BW' + operand

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'BW' + getopr(data.Arguments[0])


def scp_QueueWorkItem(data):
    return scp_lambda_worker(data, 1)               # ExitThread

def scp_QueueWorkItem2(data):
    return scp_lambda_worker(data, 1 + 3)       # Yield, Jump(Offset)


def scp_RunExpression(data):

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction
        ins.Operand = data.TableEntry.GetAllOperand('W', fs)
        ins.Operand.append(ParseScpExpression(data))

        ins.OperandFormat = 'WE'

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'WE'

def scp_4f(data):

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction
        ins.Operand.append(fs.ReadByte())
        ins.Operand.append(ParseScpExpression(data))

        ins.OperandFormat = 'BE'

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'BE'

def scp_51(data):

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        ins.Operand = data.TableEntry.GetAllOperand('WB', fs)
        ins.Operand.append(ParseScpExpression(data))

        ins.OperandFormat = 'WBE'

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'WBE'

def scp_anonymous_talk(data):
    if data.Reason == HANDLER_REASON_FORMAT:
        return FormatFuncString(data, data.Instruction.OperandFormat)

def scp_create_chr_talk(data):
    if data.Reason == HANDLER_REASON_FORMAT:
        return FormatFuncString(data, data.Instruction.OperandFormat)

def scp_create_npc_talk(data):
    if data.Reason == HANDLER_REASON_FORMAT:
        return FormatFuncString(data, data.Instruction.OperandFormat)

def scp_create_menu(data):
    # max 10 line ?
    if data.Reason == HANDLER_REASON_FORMAT:
        return FormatFuncString(data, data.Instruction.OperandFormat, -1)

def scp_76(data):

    def getopr(opr3):
        operand = ''
        if opr3 == 0 or \
           opr3 == 1 or \
           opr3 == 3:

            operand = 'L'

        elif opr3 == 2:

            operand = 'S'

        return operand

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        ins.Operand = data.TableEntry.GetAllOperand('BSB', fs)

        opr3 = ins.Operand[2]

        operand = getopr(opr3)
        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        ins.OperandFormat = 'BSB' + operand

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        opr3 = data.Arguments[2]

        data.Instruction.OperandFormat = 'BSB' + getopr(opr3)

def scp_98(data):

    def getopr(opr1):
        operand = ''
        if opr1 == 0:
            operand = 'W'

        elif opr1 == 1:
            operand = 'LLL'

        else:
            operand = 'WLB'

        return operand

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        opr = 'B'
        ins.OperandFormat = opr
        ins.Operand = data.TableEntry.GetAllOperand(opr, fs)

        operand = getopr(ins.Operand[0])
        ins.OperandFormat += operand
        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        opr1 = data.Arguments[0]

        data.Instruction.OperandFormat = 'B' + getopr(opr1)

def scp_c9(data):

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        opr = 'BB'
        ins.OperandFormat = opr
        ins.Operand = data.TableEntry.GetAllOperand(opr, fs)

        opr = 'W' * ins.Operand[1]
        ins.OperandFormat += opr
        ins.Operand += data.TableEntry.GetAllOperand(opr, fs)

        while True:
            ins.OperandFormat += 'W'
            ins.Operand += data.TableEntry.GetAllOperand('W', fs)
            if ins.Operand[-1] == 0xFFFF:
                break

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        opr2 = data.Arguments[1]
        data.Instruction.OperandFormat = 'BB' +  'W' * opr2

        i = opr2 + 2
        while True:
            data.Instruction.OperandFormat += 'W'
            if data.Arguments[i] == 0xFFFF:
                break
            i += 1

def scp_cb(data):

    def getopr(opr1):
        operand = ''
        if opr1 != 0:
            operand = 'B'

        return operand

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        opr = 'BB'
        ins.OperandFormat = opr
        ins.Operand = data.TableEntry.GetAllOperand(opr, fs)

        operand = getopr(ins.Operand[0])
        ins.OperandFormat += operand
        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        opr1 = data.Arguments[0]

        data.Instruction.OperandFormat = 'BB' + getopr(opr1)

def scp_cc(data):

    def getopr(opr1):
        operand = ''
        if opr1 == 0:
            operand = 'WWB'

        elif opr1 == 1:
            operand = 'S'

        elif opr1 == 3:
            operand = 'B'

        return operand

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        opr = 'BB'
        ins.OperandFormat = opr
        ins.Operand = data.TableEntry.GetAllOperand(opr, fs)

        operand = getopr(ins.Operand[0])
        ins.OperandFormat += operand
        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        opr1 = data.Arguments[0]

        data.Instruction.OperandFormat = 'BB' + getopr(opr1)

def scp_ce(data):

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction
        ins.Operand.append(fs.ReadByte())
        ins.Operand.append(ParseScpExpression(data))

        ins.OperandFormat = 'BE'

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'BE'

def scp_d9(data):
    def getopr(opr1):
        return 'S' if opr1 == 0 else ''

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        ins.OperandFormat = 'B'
        ins.Operand = data.TableEntry.GetAllOperand(ins.OperandFormat, fs)

        opr = getopr(ins.Operand[0])

        if len(opr) > 0:
            ins.OperandFormat += opr
            ins.Operand  += data.TableEntry.GetAllOperand(opr, fs)

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat =  'B' + getopr(data.Arguments[0])

def scp_dc(data): 
    def getopr(opr1):
        if opr1 == 1:
            return 'B'
        return ''

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        opr = 'BB'
        ins.OperandFormat = opr
        ins.Operand = data.TableEntry.GetAllOperand(opr, fs)

        operand = getopr(ins.Operand[0])
        ins.OperandFormat += operand
        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        opr1 = data.Arguments[0]

        data.Instruction.OperandFormat = 'BB' + getopr(opr1)

def scp_e2(data): 
    def getopr(opr1):
        if opr1 == 0 or opr1 == 2 or opr1 == 3 or opr1 == 4 or opr1 == 9 or opr1 == 11:
            return 'B'
        elif opr1 == 5:
            return 'IB'
        elif opr1 == 6:
            return 'H'
        return ''

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        opr = 'B'
        ins.OperandFormat = opr
        ins.Operand = data.TableEntry.GetAllOperand(opr, fs)

        operand = getopr(ins.Operand[0])
        ins.OperandFormat += operand
        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        opr1 = data.Arguments[0]

        data.Instruction.OperandFormat = 'B' + getopr(opr1)

def scp_e3(data): 
    def getopr(opr1):
        if opr1 == 0:
            return 'BIB'
        elif opr1 == 1:
            return 'B'
        elif opr1 == 4:
            return 'BB'
        elif opr1 == 5:
            return 'B'
        return ''

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        opr = 'B'
        ins.OperandFormat = opr
        ins.Operand = data.TableEntry.GetAllOperand(opr, fs)

        operand = getopr(ins.Operand[0])
        ins.OperandFormat += operand
        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        opr1 = data.Arguments[0]

        data.Instruction.OperandFormat = 'B' + getopr(opr1)

def scp_e5(data): 
    def getopr(opr1):
        return 'I' if opr1 == 0 or opr1 == 1 or opr1 == 2 else ''

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        opr = 'BBB'
        ins.OperandFormat = opr
        ins.Operand = data.TableEntry.GetAllOperand(opr, fs)

        operand = getopr(ins.Operand[0])
        ins.OperandFormat += operand
        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        opr1 = data.Arguments[0]

        data.Instruction.OperandFormat = 'BBB' + getopr(opr1)

def scp_e6(data): 
    def getopr(opr1):
        return 'B' if opr1 == 0 or opr1 == 1 else ''

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        opr = 'B'
        ins.OperandFormat = opr
        ins.Operand = data.TableEntry.GetAllOperand(opr, fs)

        operand = getopr(ins.Operand[0])
        ins.OperandFormat += operand
        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        opr1 = data.Arguments[0]

        data.Instruction.OperandFormat = 'B' + getopr(opr1)

def MakeScenarioFlags(offset, bit):
    return (offset << 3) | (bit & 7)

def SplitScenarioFlags(flags):
    return (flags >> 3), (flags & 7)

def scp_set_scenario_flags(data):

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        offset, bit = SplitScenarioFlags(data.TableEntry.GetOperand('W', fs))

        ins.Operand = [offset, bit]
        ins.OperandFormat = 'WC'

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'W'

        if len(data.Arguments) == 2:
            offset, bit = data.Arguments[0], data.Arguments[1]
            if offset >= 0x220:
                raise Exception('offset must be less than 0x220')

            data.Arguments = [MakeScenarioFlags(offset, bit)]

def scp_clear_scenario_flags(data):
    return scp_set_scenario_flags(data)


def scp_fe(data):
    print('scp_fe reason', data.Reason)
    if data.Reason == HANDLER_REASON_FORMAT:
        print('fe?')
        return FormatFuncString(data, data.Instruction.OperandFormat, -1)


ed63rd_op_list = \
[
    inst(ExitThread),                                                                                   # 00
    inst(Return,                    NO_OPERAND,             INSTRUCTION_END_BLOCK),                     # 01
    inst(Jc,                        NO_OPERAND,             INSTRUCTION_START_BLOCK,    scp_if),        # 02
    inst(Jump,                      'O',                    INSTRUCTION_JUMP),                          # 03
    inst(Switch,                    NO_OPERAND,             INSTRUCTION_END_BLOCK,      scp_switch),    # 04
    inst(Call,                      'CH'),          # Call(scp index, func index)                       # 05
    inst(NewScene,                  NO_OPERAND,             0,                          scp_new_scene), # 06
    inst(IdleLoop),                         # 07
    inst(Sleep,                     'I'),   # 08
    inst(SetMapFlags,               'L'),   # 09
    inst(ClearMapFlags,             'L'),   # 0A
    inst(FadeToDark,                'iic'), # 0B
    inst(FadeToBright,              'ii'),  # 0C
    inst(OP_0D),
    inst(Fade,                      'I'),                                                                 # 0E
    inst(Battle,                    'LLBWB'),   #,             0,                          scp_battle),   # 0F
    inst(OP_10,                     'BB'),
    inst(OP_11,                     'BBBLLL'),
    inst(StopSound,                 'LLL'),         # 12
    inst(SetPlaceName,              'W'),           # 13
    inst(BlurSwitch,                'LLLBL'),       # 14 
    inst(OP_15,                     'L'),
    inst(OP_16,                     NO_OPERAND,             0,                          scp_16),
    inst(ShowSaveMenu, 'B'),                             # 17 
    inst(OP_18),
    inst(EventBegin,                'B'),           # 19 
    inst(EventEnd,                  'B'),           # 1A  
    inst(OP_1B,                     'BBW'),
    inst(OP_1C,                     'BBW'),
    inst(OP_1D,                     'B'),
    inst(OP_1E),
    inst(OP_1F,                     'BL'),
    inst(OP_20,                     'L'),
    inst(OP_21),
    inst(OP_22,                     'WBB'),
    inst(OP_23,                     'W'),
    inst(OP_24,                     'WB'),
    inst(SoundDistance,             'WLLLLLBL'),    # 25
    inst(SoundLoad,                 'H'),           # 26
    inst(Yield),                                    # 27
    inst(OP_28,                     NO_OPERAND,             0,                          scp_28),
    inst(OP_29,                     NO_OPERAND,             0,                          scp_29),
    inst(OP_2A,                     NO_OPERAND,             0,                          scp_2a),
    inst(OP_2B,                     'WW'),
    inst(OP_2C,                     'WW'),
    inst(AddParty,                  'BBB'), # 2D
    inst(RemoveParty,               'BB'),  # 2E
    inst(ClearParty),                       # 2F
    inst(OP_30,                     'B'),
    inst(OP_31,                     'BBW'),
    inst(OP_32,                     'BW'),
    inst(OP_33,                     'BW'),
    inst(OP_34,                     'BW'),
    inst(OP_35,                     'BW'),
    inst(OP_36,                     'BW'),
    inst(OP_37,                     NO_OPERAND,             0,                          scp_37),
    inst(AddSepith,                 'BW'),      # AddSepith(0~6, number)      # 38
    inst(SubSepith,                 'BW'),                                    # 39
    inst(AddMira,                   'H'),                                     # 3A
    inst(SubMira,                   'H'),                                     # 3B
    inst(OP_3C,                     'H'),
    inst(OP_3D,                     'H'),
    inst(OP_3E,                     'Wh'),
    inst(OP_3F,                     'Wh'),
    inst(OP_40,                     'WB'),
    inst(OP_41,                     'BWB'),
    inst(OP_42,                     'B'),
    inst(OP_43,                     'WBBW'),
    inst(OP_44,                     'WB'),
    inst(QueueWorkItem,             NO_OPERAND,     0,                                  scp_QueueWorkItem),     # 45
    inst(QueueWorkItem2,            NO_OPERAND,     0,                                  scp_QueueWorkItem2),    # 46
    inst(WaitChrThread,             'WW'),  # 47
    inst(OP_48),
    inst(Event,                     'CH'),  # 49
    inst(OP_4A,                     'WC'),
    inst(OP_4B,                     'WC'),
    inst(OP_4C),
    inst(RunExpression,             NO_OPERAND,     0,                                  scp_RunExpression),     # 4D
    inst(OP_4E),
    inst(OP_4F,                     NO_OPERAND,     0,                                  scp_4f),
    inst(OP_50),
    inst(OP_51,                     NO_OPERAND,     0,                                  scp_51),
    inst(TalkBegin,                 'W'),   # 52
    inst(TalkEnd,                   'W'),   # 53
    inst(AnonymousTalk,             'S',            0,                                  scp_anonymous_talk),    # 54
    inst(OP_55),
    inst(OP_56,                     'B'),
    inst(OP_57,                     'WWWS'),
    inst(CloseMessageWindow),       # 58
    inst(OP_59),
    inst(SetMessageWindowPos,       'hhhh'),        # SetMessageWindowPos(x, y, -1, -1)                         # 5A
    inst(ChrTalk,                   'WS',           0,                                  scp_create_chr_talk),   # 5B
    inst(NpcTalk,                   'WSS',          0,                                  scp_create_npc_talk),   # 5C
    inst(Menu,                      'hhhcS',        0,                                  scp_create_menu),       # 5D
    inst(MenuEnd,                   'W'),                                                                       # 5E
    inst(OP_5F,                     'W'),
    inst(SetChrName,                'S'),           # 60
    inst(OP_61,                     'W'),
    inst(OP_62,                     'WLIBBLB'),
    inst(OP_63,                     'W'),
    inst(OP_64,                     'BW'),
    inst(OP_65,                     'BW'),
    inst(OP_66,                     'W'),
    inst(OP_67,                     'iiii'),
    inst(OP_68,                     'W'),
    inst(OP_69,                     'WL'),
    inst(OP_6A,                     'W'),
    inst(OP_6B,                     'ii'),          # SetCameraDistance(distance, duration)
    inst(OP_6C,                     'ii'),
    inst(OP_6D,                     'iiii'),
    inst(OP_6E,                     'ii'),
    inst(OP_6F,                     'Wi'),
    inst(OP_70,                     'WL'),
    inst(OP_71,                     'WWB'),
    inst(OP_72,                     'WWB'),
    inst(OP_73,                     'W'),
    inst(OP_74,                     'WLW'),
    inst(OP_75,                     'BLB'),
    inst(OP_76,                     'WLWLLLBB'),
    inst(OP_77,                     'BBBBL'),
    inst(OP_78,                     'BBB'),
    inst(OP_79,                     'BW'),
    inst(OP_7A,                     'BW'),
    inst(OP_7B),
    inst(OP_7C,                     'LLLL'),
    inst(OP_7D,                     'BWWW'),
    inst(OP_7E,                     'WWWBL'),
    inst(LoadEffect,                'BS'),                  #7F
    inst(PlayEffect,                'BBWiiihhhiiiwiiii'),   #80   
    inst(Play3DEffect,              'BBBSLLLWWWLLLL'),      #81
    inst(OP_82,                     'BB'),
    inst(OP_83,                     'BB'),
    inst(OP_84,                     'B'),
    inst(OP_85,                     'W'),
    inst(SetChrChipByIndex,         'WH'),       # 86
    inst(SetChrSubChip,             'WH'),       # 87
    inst(SetChrPos,                 'Wiiih'),    # 88
    inst(OP_89,                     'Wiiih'),
    inst(TurnDirection,             'WWH'),      # 8A
    inst(OP_8B,                     'WLLW'),
    inst(OP_8C,                     'Whh'),
    inst(OP_8D,                     'Wiiiii'),
    inst(OP_8E,                     'WLLLLB'),
    inst(OP_8F,                     'WLLLLB'),
    inst(OP_90,                     'WLLLLB'),
    inst(OP_91,                     'WLLLLB'),
    inst(OP_92,                     'WWLLB'),
    inst(OP_93,                     'WWLLB'),
    inst(OP_94,                     'BWWLLB'),
    inst(OP_95,                     'WLLLLL'),
    inst(OP_96,                     'WLLLLL'),
    inst(OP_97,                     'WLLLLW'),
    inst(OP_98,                     NO_OPERAND,     0,                                  scp_98),
    inst(OP_99,                     'WBBL'),
    inst(SetChrFlags,               'WW'),      # 9A
    inst(ClearChrFlags,             'WW'),      # 9B
    inst(SetChrBattleFlags,         'WW'),      # 9C
    inst(ClearChrBattleFlags,       'WW'),      # 9D
    inst(OP_9E,                     'WLLLL'),
    inst(OP_9F,                     'WBBBBL'),
    inst(OP_A0,                     'WBBBL'),
    inst(OP_A1,                     'WW'),
    inst(OP_A2,                     'W'),
    inst(OP_A3,                     'W'),
    inst(OP_A4,                     'B' * 2),
    inst(OP_A5,                     'W'),
    inst(OP_A6,                     'W'),
    inst(OP_A7,                     'WW'),
    inst(OP_A8,                     'B' * 5),
    inst(OP_A9,                     'B'),
    inst(OP_AA,                     'I'),
    inst(OP_AB),
    inst(OP_AC,                     'W'),
    inst(OP_AD,                     'LWWL'),
    inst(OP_AE,                     'L'),
    inst(OP_AF,                     'BW'),
    inst(OP_B0,                     'WB'),
    inst(OP_B1,                     'S'),
    inst(OP_B2,                     'BBW'),
    inst(PlayMovie,                 'BSWW'),    # B3
    inst(OP_B4,                     'B'),
    inst(OP_B5,                     'B'),
    inst(OP_B6,                     'WB'),
    inst(OP_B7,                     'B'),
    inst(OP_B8,                     'WW'),
    inst(OP_B9,                     'BW'),
    inst(OP_BA,                     'BB'),
    inst(OP_BB,                     'BBL'),
    inst(OP_BC,                     'BBW'),
    inst(OP_BD),
    inst(OP_BE,                     'BBWWWBiiiiii'),
    inst(OP_BF,                     'BBHH'),
    inst(OP_C0,                     'BLLLLLLLL'),
    inst(OP_C1,                     'BBL'),
    inst(OP_C2,                     'BB'),
    inst(OP_C3,                     'W'),
    inst(OP_C4,                     'BL'),
    inst(OP_C5,                     'BWWWWWWWWWWWWLBS'),
    inst(OP_C6,                     'BBiii'),
    inst(OP_C7,                     'BBB'),
    inst(OP_C8,                     'WWSBW'),
    inst(OP_C9,                     NO_OPERAND,     0,                                  scp_c9),
    inst(OP_CA,                     'BBBBBBBBBB'),
    inst(OP_CB,                     NO_OPERAND,     0,                                  scp_cb),
    inst(OP_CC,                     NO_OPERAND,     0,                                  scp_cc),
    inst(OP_CD,                     'W'),
    inst(OP_CE,                     NO_OPERAND,     0,                                  scp_ce),
    inst(OP_CF,                     'WBS'),
    inst(OP_D0,                     'ii'),
    inst(OP_D1,                     'hiiii'),
    inst(OP_D2,                     'LLB'),
    inst(OP_D3,                     'B'),
    inst(OP_D4,                     'BB'),
    inst(OP_D5,                     'BB'),
    inst(OP_D6,                     'B'),
    inst(OP_D7,                     'Bih'),
    inst(OP_D8,                     'BW'),
    inst(OP_D9,                     NO_OPERAND,     0,                                  scp_d9),
    inst(OP_DA),
    inst(OP_DB,                     'BB'),
    inst(OP_DC,                     NO_OPERAND,     0,                                  scp_dc),
    inst(OP_DD,                     'BBBIIII'),
    inst(OP_DE,                     'BBB'),
    inst(OP_DF,                     'BBB'),
    inst(OP_E0,                     'HBB'),
    inst(OP_E1,                     'BB'),
    inst(OP_E2,                     NO_OPERAND,     0,                                  scp_e2),
    inst(OP_E3,                     NO_OPERAND,     0,                                  scp_e3),
    inst(OP_E4,                     'B' * 4),
    inst(OP_E5,                     NO_OPERAND,     0,                                  scp_e5),
    inst(OP_E6,                     NO_OPERAND,     0,                                  scp_e6),
    inst(OP_E7,                     'BBBBBBI'),
    inst(OP_EA),
    inst(OP_F7,                     'BWB'),

    inst(OP_E8,                     ''),
    inst(OP_E9,                     ''),
    inst(OP_ED,                     'BBBBBBBBBBBBB'),
    inst(OP_F0,                     'BBBB'),
    inst(OP_F1,                     'BBB'),
    inst(OP_F2,                     'BBBBBBB'),
    inst(OP_F3,                     'BB'),
    inst(OP_F5,                     'BBBB'),
    inst(OP_F8,                     'W'),
    inst(OP_F9,                     'BBB'),
    inst(OP_FA,                     'BBBBBB'),
    inst(OP_FB,                     'BBBB'),
    inst(OP_FC,                     'BB'),
    inst(OP_FD,                     'W'),
    inst(OP_FE,                     'S',                    0,                           scp_fe),
]

del inst

for op in ed63rd_op_list:
    ed63rd_op_table[op.OpCode] = op
    op.Container = ed63rd_op_table



'''

MenuCmd(0x0, 1)
cmd: 0 = create
layer: 1

MenuCmd(0x1, 1, '莉夏')
cmd: 1 = add item
layer: 1
text:

MenuCmd(0x2, 1, 15, 45, 0x1)
cmd: 2 = show
layer: 1
x: 15
y: 45
unknown: 1



羁绊
OP_50(chr_offset, (scpexpr(EXPR_PUSH_LONG, const), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
0x64: 琪雅
0x65: 艾莉
0x66: 缇欧
0x67: 兰迪
0x68: 诺艾尔
0x69: 瓦吉
0x6A: 莉夏
0x6C: 伊莉娅
0x6D: 塞茜尔
0x6E: 芙兰
0x6F: 修利

'''




if __name__ == '__main__':
    valid = 0
    for inst in ed63rd_op_list:
        if inst.OpName[:3] != 'OP_':
            valid += 1
    print('known: %d (%d%%)' % (valid, valid / len(ed63rd_op_list) * 100))
    print('total: %d' % len(ed63rd_op_list))
    console.pause()
