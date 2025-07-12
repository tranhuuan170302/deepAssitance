from typing import Optional, Sequence, List, Any
import llama_index
from llama_index.core.embeddings.utils import EmbedType
from llama_index.core.data_structs.data_structs import IndexDict, IndexGraph
from llama_index.core.schema import (
    BaseNode,
    Document,
    ImageNode,
    MetadataMode,
    IndexNode,
    TextNode,
    TransformComponent,
)
from llama_index.core.storage.storage_context import StorageContext
from llama_index.core.callbacks.base import CallbackManager


class VectorStoreIndex(llama_index.core.VectorStoreIndex):

    def __init__(
        self,
        nodes: Optional[Sequence[BaseNode]] = None,
        use_async: bool = False,
        store_nodes_override: bool = False,
        embed_model: Optional[EmbedType] = None,
        insert_batch_size: int = 2048,
        objects: Optional[Sequence[IndexNode]] = None,
        index_struct: Optional[IndexDict] = None,
        storage_context: Optional[StorageContext] = None,
        callback_manager: Optional[CallbackManager] = None,
        transformations: Optional[List[TransformComponent]] = None,
        show_progress: bool = True,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            nodes=nodes,
            use_async=use_async,
            store_nodes_override=store_nodes_override,
            embed_model=embed_model,
            insert_batch_size=insert_batch_size,
            objects=objects,
            index_struct=index_struct,
            storage_context=storage_context,
            callback_manager=callback_manager,
            transformations=transformations,
            **kwargs,
        )

    def _build_index_from_index(
        self,
        nodes: Sequence[BaseNode],
        **insert_kwargs: Any,
    ) -> None:
        return super()._build_index_from_index(nodes, **insert_kwargs)
