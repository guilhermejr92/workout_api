from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from workout_api.contrib.models import BaseModel


class AtletaModel(BaseModel):
    __tablename__ = 'atletas'

    pk_id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    idade = Column(Integer, nullable=False)
    peso = Column(Float, nullable=False)
    altura = Column(Float, nullable=False)
    sexo = Column(String(1), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    categoria_id = Column(Integer, ForeignKey("categorias.pk_id"))
    categoria = relationship(
        "CategoriaModel", back_populates="atleta", lazy='selectin')
    centro_treinamento_id = Column(
        Integer, ForeignKey("centros_treinamento.pk_id"))
    centro_treinamento = relationship(
        "CentroTreinamentoModel", back_populates="atleta", lazy='selectin')
