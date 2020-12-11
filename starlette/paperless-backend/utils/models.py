from sqlalchemy import Column, Integer, String, TIMESTAMP, DateTime, BLOB, Boolean, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

metadata = MetaData()

to_association_table = Table('to_association', metadata,
    Column('job_id', Integer, ForeignKey('joballotment.job_id')),
    Column('allotted_to', Integer, ForeignKey('users.uid'))
)

by_association_table = Table('by_association', metadata,
    Column('job_id', Integer, ForeignKey('joballotment.job_id')),
    Column('allotted_by', Integer, ForeignKey('users.uid')),
)


users = Table(
    'users',
    metadata,
    Column('uid', Integer, primary_key = True),
    Column('uname', String),
    Column('role', String),
    Column('password', String),
    Column('department', String),
    Column('email', String),
    Column('created_at', TIMESTAMP),
    Column('linkedin', String),
    Column('twitter', String),
    Column('phone', String),
    Column('city', String),
    
)

manual = Table(
    'manual',
    metadata,
    Column('man_id', Integer, primary_key = True),
    Column('uploaded_by', Integer, ForeignKey('users.uid')),
    Column('date', DateTime),
    Column('title', String),
    Column('document', String),
    Column('department', String)

)

joballotment = Table(
    'joballotment',
    metadata,
    Column('job_id', Integer, primary_key = True),
    Column('alloted_to', Integer, ForeignKey('to_association.allotted_to')),
    Column('alloted_by', Integer, ForeignKey('by_association.allotted_by')),
    Column('allotment_date', DateTime),
    Column('submission_date', DateTime),
    Column('title', String),
    Column('task', String),
    Column('submission', String),
    Column('review', String),
    Column('reply', String),
    Column('approved_status', Boolean),
    
)


