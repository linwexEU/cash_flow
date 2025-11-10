from datetime import datetime, timezone

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Index, ForeignKey, TIMESTAMP

from src.db.base import Base


class CashStatus(Base): 
    __tablename__ = "cash_status"

    id: Mapped[int] = mapped_column(primary_key=True)
    status_name: Mapped[str] = mapped_column(unique=True, nullable=False)

    __table_args__ = (
        Index("ix_cash_status_status_name", status_name),
    )


class CashType(Base): 
    __tablename__ = "cash_type"

    id: Mapped[int] = mapped_column(primary_key=True) 
    type_name: Mapped[str] = mapped_column(unique=True, nullable=False)

    category = relationship("Category", back_populates="type_")

    __table_args__ = (
        Index("ix_cash_type_type_name", type_name),
    )


class Category(Base): 
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True)
    category_name: Mapped[str] = mapped_column(unique=True, nullable=False)
    cash_type: Mapped[int] = mapped_column(ForeignKey("cash_type.id"), nullable=False)

    type_ = relationship("CashType", back_populates="category")
    subcategory = relationship("SubCategory", back_populates="category")

    __table_args__ = (
        Index("ix_category_category_name", category_name),
    )
    

class SubCategory(Base): 
    __tablename__ = "subcategory"

    id: Mapped[int] = mapped_column(primary_key=True)
    subcategory_name: Mapped[str] = mapped_column(unique=True, nullable=False) 
    parent_category: Mapped[int] = mapped_column(ForeignKey("category.id"), nullable=False)

    category = relationship("Category", back_populates="subcategory", cascade="all, delete")

    __table_args__ = (
        Index("ix_subcategory_subcategory_name", subcategory_name),
    )


class CashFlow(Base): 
    __tablename__ = "cash_flow"

    id: Mapped[int] = mapped_column(primary_key=True)
    create_utc: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), default=datetime.now(timezone.utc))
    cash_status: Mapped[int] = mapped_column(ForeignKey("cash_status.id"), nullable=False)
    cash_type: Mapped[int] = mapped_column(ForeignKey("cash_type.id"), nullable=False) 
    amount: Mapped[float] = mapped_column(nullable=False)
    category: Mapped[int] = mapped_column(ForeignKey("category.id"), nullable=False)
    comment: Mapped[str] = mapped_column(nullable=True)

    cash_status_rel = relationship("CashStatus")
    cash_type_rel = relationship("CashType") 
    category_rel = relationship("Category")
    subcategories_rel = relationship("SubCategory", secondary="category")

    __table_args__ = (
        Index("ix_cash_flow_create_utc", create_utc),
        Index("ix_cash_flow_cash_status", cash_status),
        Index("ix_cash_flow_cash_type", cash_type),
        Index("ix_cash_flow_category", category)
    )
