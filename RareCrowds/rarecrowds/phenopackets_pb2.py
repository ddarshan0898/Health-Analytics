# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: phenopackets.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import rarecrowds.base_pb2 as base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="phenopackets.proto",
    package="org.phenopackets.schema.v1",
    syntax="proto3",
    serialized_options=b"\n\032org.phenopackets.schema.v1P\001",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b"\n\x12phenopackets.proto\x12\x1aorg.phenopackets.schema.v1\x1a\nbase.proto\"\x91\x04\n\x0bPhenopacket\x12\n\n\x02id\x18\x01 \x01(\t\x12<\n\x07subject\x18\x02 \x01(\x0b\x32+.org.phenopackets.schema.v1.core.Individual\x12O\n\x13phenotypic_features\x18\x03 \x03(\x0b\x32\x32.org.phenopackets.schema.v1.core.PhenotypicFeature\x12>\n\nbiosamples\x18\x04 \x03(\x0b\x32*.org.phenopackets.schema.v1.core.Biosample\x12\x34\n\x05genes\x18\x05 \x03(\x0b\x32%.org.phenopackets.schema.v1.core.Gene\x12:\n\x08variants\x18\x06 \x03(\x0b\x32(.org.phenopackets.schema.v1.core.Variant\x12:\n\x08\x64iseases\x18\x07 \x03(\x0b\x32(.org.phenopackets.schema.v1.core.Disease\x12;\n\thts_files\x18\x08 \x03(\x0b\x32(.org.phenopackets.schema.v1.core.HtsFile\x12<\n\tmeta_data\x18\t \x01(\x0b\x32).org.phenopackets.schema.v1.core.MetaData\"\xc2\x02\n\x06\x46\x61mily\x12\n\n\x02id\x18\x01 \x01(\t\x12\x38\n\x07proband\x18\x02 \x01(\x0b\x32'.org.phenopackets.schema.v1.Phenopacket\x12:\n\trelatives\x18\x03 \x03(\x0b\x32'.org.phenopackets.schema.v1.Phenopacket\x12;\n\x08pedigree\x18\x04 \x01(\x0b\x32).org.phenopackets.schema.v1.core.Pedigree\x12;\n\thts_files\x18\x05 \x03(\x0b\x32(.org.phenopackets.schema.v1.core.HtsFile\x12<\n\tmeta_data\x18\x06 \x01(\x0b\x32).org.phenopackets.schema.v1.core.MetaData\"\xde\x01\n\x06\x43ohort\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x38\n\x07members\x18\x03 \x03(\x0b\x32'.org.phenopackets.schema.v1.Phenopacket\x12;\n\thts_files\x18\x04 \x03(\x0b\x32(.org.phenopackets.schema.v1.core.HtsFile\x12<\n\tmeta_data\x18\x05 \x01(\x0b\x32).org.phenopackets.schema.v1.core.MetaDataB\x1e\n\x1aorg.phenopackets.schema.v1P\x01\x62\x06proto3",
    dependencies=[
        base__pb2.DESCRIPTOR,
    ],
)


_PHENOPACKET = _descriptor.Descriptor(
    name="Phenopacket",
    full_name="org.phenopackets.schema.v1.Phenopacket",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="org.phenopackets.schema.v1.Phenopacket.id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="subject",
            full_name="org.phenopackets.schema.v1.Phenopacket.subject",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="phenotypic_features",
            full_name="org.phenopackets.schema.v1.Phenopacket.phenotypic_features",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="biosamples",
            full_name="org.phenopackets.schema.v1.Phenopacket.biosamples",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="genes",
            full_name="org.phenopackets.schema.v1.Phenopacket.genes",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="variants",
            full_name="org.phenopackets.schema.v1.Phenopacket.variants",
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="diseases",
            full_name="org.phenopackets.schema.v1.Phenopacket.diseases",
            index=6,
            number=7,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="hts_files",
            full_name="org.phenopackets.schema.v1.Phenopacket.hts_files",
            index=7,
            number=8,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="meta_data",
            full_name="org.phenopackets.schema.v1.Phenopacket.meta_data",
            index=8,
            number=9,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=63,
    serialized_end=592,
)


_FAMILY = _descriptor.Descriptor(
    name="Family",
    full_name="org.phenopackets.schema.v1.Family",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="org.phenopackets.schema.v1.Family.id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="proband",
            full_name="org.phenopackets.schema.v1.Family.proband",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="relatives",
            full_name="org.phenopackets.schema.v1.Family.relatives",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="pedigree",
            full_name="org.phenopackets.schema.v1.Family.pedigree",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="hts_files",
            full_name="org.phenopackets.schema.v1.Family.hts_files",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="meta_data",
            full_name="org.phenopackets.schema.v1.Family.meta_data",
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=595,
    serialized_end=917,
)


_COHORT = _descriptor.Descriptor(
    name="Cohort",
    full_name="org.phenopackets.schema.v1.Cohort",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="org.phenopackets.schema.v1.Cohort.id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="description",
            full_name="org.phenopackets.schema.v1.Cohort.description",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="members",
            full_name="org.phenopackets.schema.v1.Cohort.members",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="hts_files",
            full_name="org.phenopackets.schema.v1.Cohort.hts_files",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="meta_data",
            full_name="org.phenopackets.schema.v1.Cohort.meta_data",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=920,
    serialized_end=1142,
)

_PHENOPACKET.fields_by_name["subject"].message_type = base__pb2._INDIVIDUAL
_PHENOPACKET.fields_by_name[
    "phenotypic_features"
].message_type = base__pb2._PHENOTYPICFEATURE
_PHENOPACKET.fields_by_name["biosamples"].message_type = base__pb2._BIOSAMPLE
_PHENOPACKET.fields_by_name["genes"].message_type = base__pb2._GENE
_PHENOPACKET.fields_by_name["variants"].message_type = base__pb2._VARIANT
_PHENOPACKET.fields_by_name["diseases"].message_type = base__pb2._DISEASE
_PHENOPACKET.fields_by_name["hts_files"].message_type = base__pb2._HTSFILE
_PHENOPACKET.fields_by_name["meta_data"].message_type = base__pb2._METADATA
_FAMILY.fields_by_name["proband"].message_type = _PHENOPACKET
_FAMILY.fields_by_name["relatives"].message_type = _PHENOPACKET
_FAMILY.fields_by_name["pedigree"].message_type = base__pb2._PEDIGREE
_FAMILY.fields_by_name["hts_files"].message_type = base__pb2._HTSFILE
_FAMILY.fields_by_name["meta_data"].message_type = base__pb2._METADATA
_COHORT.fields_by_name["members"].message_type = _PHENOPACKET
_COHORT.fields_by_name["hts_files"].message_type = base__pb2._HTSFILE
_COHORT.fields_by_name["meta_data"].message_type = base__pb2._METADATA
DESCRIPTOR.message_types_by_name["Phenopacket"] = _PHENOPACKET
DESCRIPTOR.message_types_by_name["Family"] = _FAMILY
DESCRIPTOR.message_types_by_name["Cohort"] = _COHORT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Phenopacket = _reflection.GeneratedProtocolMessageType(
    "Phenopacket",
    (_message.Message,),
    {
        "DESCRIPTOR": _PHENOPACKET,
        "__module__": "phenopackets_pb2"
        # @@protoc_insertion_point(class_scope:org.phenopackets.schema.v1.Phenopacket)
    },
)
_sym_db.RegisterMessage(Phenopacket)

Family = _reflection.GeneratedProtocolMessageType(
    "Family",
    (_message.Message,),
    {
        "DESCRIPTOR": _FAMILY,
        "__module__": "phenopackets_pb2"
        # @@protoc_insertion_point(class_scope:org.phenopackets.schema.v1.Family)
    },
)
_sym_db.RegisterMessage(Family)

Cohort = _reflection.GeneratedProtocolMessageType(
    "Cohort",
    (_message.Message,),
    {
        "DESCRIPTOR": _COHORT,
        "__module__": "phenopackets_pb2"
        # @@protoc_insertion_point(class_scope:org.phenopackets.schema.v1.Cohort)
    },
)
_sym_db.RegisterMessage(Cohort)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)